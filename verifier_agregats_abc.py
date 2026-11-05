"""Check published thesis aggregates, not original observations or experiments.

Created for the scientific clarification of the manuscript. This is not the
original R analysis script. Python 3.9 or later, standard library only.
"""

import argparse
import hashlib
import itertools
import json
import math
import re
import sys
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import BadZipFile, ZipFile


W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(element):
    return "".join(node.text or "" for node in element.iter(W + "t"))


def rows(table):
    return [
        [text(cell).strip() for cell in row.findall(W + "tc")]
        for row in table.findall(W + "tr")
    ]


def rounded(value, places):
    value = Fraction(value)
    decimal = Decimal(value.numerator) / Decimal(value.denominator)
    return decimal.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP)


def solve_unique(matrix, targets):
    require(bool(matrix), "The linear system is empty.")
    columns = len(matrix[0])
    require(columns > 0, "The linear system has no variables.")
    require(len(matrix) == len(targets), "Incompatible matrix and target sizes.")
    require(all(len(row) == columns for row in matrix), "The matrix is not rectangular.")
    augmented = [
        [Fraction(value) for value in row] + [Fraction(target)]
        for row, target in zip(matrix, targets)
    ]
    pivots = []
    for column in range(columns):
        pivot = next(
            (i for i in range(len(pivots), len(augmented)) if augmented[i][column]),
            None,
        )
        if pivot is None:
            continue
        position = len(pivots)
        augmented[position], augmented[pivot] = augmented[pivot], augmented[position]
        scale = augmented[position][column]
        augmented[position] = [value / scale for value in augmented[position]]
        for i in range(len(augmented)):
            if i != position:
                factor = augmented[i][column]
                augmented[i] = [
                    a - factor * b for a, b in zip(augmented[i], augmented[position])
                ]
        pivots.append(column)
    require(
        not any(not any(row[:-1]) and row[-1] for row in augmented),
        "The exact displayed values are incompatible with the linear model.",
    )
    require(len(pivots) == columns, "The exact displayed values do not uniquely identify the weights.")
    solution = [Fraction(0)] * columns
    for row, column in zip(augmented, pivots):
        solution[column] = row[-1]
    return solution


def compatible_decisions(weights, numerator):
    patterns = Counter()
    for vector in itertools.product((0, 1), repeat=len(weights)):
        if sum(weight * value for weight, value in zip(weights, vector)) != numerator:
            continue
        missing_core = sum(weight == 2 and value == 0 for weight, value in zip(weights, vector))
        missing_operational = sum(weight == 1 and value == 0 for weight, value in zip(weights, vector))
        patterns[(missing_core, missing_operational)] += 1
    return {
        "compatible_vectors": sum(patterns.values()),
        "unmet_criterion_patterns": [
            {"fundamental": core, "operational": operational, "vectors": count}
            for (core, operational), count in sorted(patterns.items())
        ],
        "individual_criteria_identifiable": False,
    }


def read_tables(path):
    with ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    body = root.find(W + "body")
    require(body is not None, "No Word document body.")
    tables = {}
    pending = None
    for element in body:
        if element.tag == W + "p":
            style = element.find(W + "pPr/" + W + "pStyle")
            if style is not None and style.get(W + "val") == "FRTableCaption":
                match = re.match(r"Tableau\s+([A-Z0-9]+\.\d+)\b", text(element))
                require(match is not None, "A table caption has no identifier.")
                pending = match[1]
        elif element.tag == W + "tbl" and pending is not None:
            require(pending not in tables, "Duplicate table identifier: " + pending)
            tables[pending] = rows(element)
            pending = None
    for identifier in ("2.8", "4.1", "4.11", "4.12", "5.3"):
        require(identifier in tables, "Missing required table: " + identifier)
    return tables


def audit(path):
    tables = read_tables(path)
    criteria = tables["2.8"]
    require(len(criteria) == 17, "Table 2.8 must contain fifteen criteria and a total.")
    weights = [int(row[-1]) for row in criteria[1:-1]]
    require(weights == [2] * 4 + [1] * 11, "Unexpected criterion weights.")
    weight_sum = sum(weights)
    declared_total = int(criteria[-1][-1])
    require(
        declared_total == weight_sum,
        f"Table 2.8: declared total {declared_total}, but the fifteen weights sum to {weight_sum}.",
    )

    survey_rows = tables["4.1"][1:]
    require(len(survey_rows) == 12, "Expected twelve published diagnostic indicators.")
    survey = []
    for row in survey_rows:
        require(len(row) == 6, "Unexpected survey table columns.")
        parsed = [re.fullmatch(r"(\d+)\s*\((\d+)%\)", cell) for cell in row[1:]]
        require(all(match is not None for match in parsed), "Invalid survey count/percentage cell.")
        counts = [int(match[1]) for match in parsed]
        percentages = [int(match[2]) for match in parsed]
        require(sum(counts) == 34, "A published diagnostic row does not total 34.")
        require(counts[2:] == [0, 0, 0], "The published absence categories have changed.")
        calculated = [int(rounded(Fraction(count, 34) * 100, 0)) for count in counts]
        require(calculated == percentages, "Inconsistent survey percentages: " + row[0])
        survey.append({"indicator": row[0], "counts": counts, "rounded_percentages": calculated})

    granularity = tables["4.11"][1:]
    require(len(granularity) == 4, "Expected four service rows.")
    matrix = [[Fraction(value) for value in row[1:5]] for row in granularity]
    scores = [Fraction(row[5]) for row in granularity]
    require(
        all(0 <= value <= 1 for row in matrix for value in row)
        and all(0 <= value <= 1 for value in scores),
        "Granularity components and scores must be within [0,1].",
    )
    inferred = solve_unique(matrix + [[1, 1, 1, 1]], scores + [1])
    require(all(value >= 0 for value in inferred) and sum(inferred) == 1, "Invalid convex weights.")
    require(
        inferred == [Fraction("0.40"), Fraction("0.30"), Fraction("0.20"), Fraction("0.10")],
        "The published reconstruction no longer matches the document.",
    )
    reproduced = [sum(a * b for a, b in zip(row, inferred)) for row in matrix]
    require(reproduced == scores, "The inferred weights do not reproduce every displayed score.")
    alternative = inferred.copy()
    alternative[0] += Fraction("0.001")
    alternative[1] -= Fraction("0.001")
    alternative_scores = [sum(a * b for a, b in zip(row, alternative)) for row in matrix]
    require(
        all(rounded(actual, 2) == rounded(expected, 2)
            for actual, expected in zip(alternative_scores, scores)),
        "The proposed example of rounded-value nonuniqueness is not compatible.",
    )

    metric_rows = tables["4.12"][1:]
    require(len(metric_rows) == 4, "Expected four architectural metric rows.")
    decisions = {}
    coupling = []
    for row in metric_rows:
        require(len(row) == 7, "Unexpected architectural metric columns.")
        fraction = Fraction(row[4])
        require(fraction.denominator == weight_sum, "A decision fraction has an unexpected denominator.")
        require(rounded(fraction, 2) == Decimal(row[5]), "A rounded decision score is inconsistent.")
        if fraction.numerator not in decisions:
            decisions[fraction.numerator] = compatible_decisions(weights, fraction.numerator)
        # The accompanying prose declares one 0.50 relation for each domain
        # service, and three synchronous relations for the BFF.
        if row[0] == "Dashboard BFF":
            numerator = Fraction(3)
        else:
            require(
                row[0] in ("Population", "Police Records", "Property Registry"),
                "Unexpected service in the coupling calculation.",
            )
            numerator = Fraction("0.50")
        ratio = numerator / (len(metric_rows) - 1)
        require(rounded(ratio, 2) == Decimal(row[2]), "A coupling ratio is inconsistent.")
        coupling.append({"service": row[0], "ratio": str(ratio), "rounded": str(rounded(ratio, 2))})
    require(decisions[18]["compatible_vectors"] == 11, "Unexpected number of 18-point vectors.")
    require(decisions[16]["compatible_vectors"] == 209, "Unexpected number of 16-point vectors.")
    criticality_sum = sum(Fraction(row[6]) for row in metric_rows)
    require(criticality_sum == 1, "The criticality weights do not sum to one.")

    expert_rows = tables["5.3"][1:]
    require(len(expert_rows) == 5, "Unexpected number of expert summary rows.")
    expert_indices = []
    for row in expert_rows[:4]:
        require(len(row) == 6, "Unexpected expert summary columns.")
        mean = Fraction(row[3])
        require(1 <= mean <= 5, "Expert mean outside the declared scale.")
        index = mean / 5 * 100
        require(index == Fraction(row[4].removesuffix("%")), "Inconsistent expert normalized index.")
        expert_indices.append({
            "panel_size_not_item_denominator": int(row[1]),
            "criterion": row[2],
            "reported_mean": row[3],
            "percent_of_scale_maximum": str(index),
            "approval_proportion": False,
        })
    require(
        expert_rows[-1][3].casefold() == "non rapport\u00e9e",
        "Usability/scalability must not be assigned an invented mean.",
    )
    return {
        "scope": "Arithmetic checks of published aggregates, not authentication of primary evidence.",
        "word_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "criterion_weight_total": weight_sum,
        "minimum_integer_points_for_threshold_0_67": math.ceil(Fraction("0.67") * weight_sum),
        "granularity": {
            "assumptions": "Common linear aggregation; displayed inputs and outputs treated as exact.",
            "compatible_weights": [str(value) for value in inferred],
            "reproduced_scores": [str(rounded(value, 2)) for value in reproduced],
            "historical_weights_authenticated": False,
            "alternative_weights_when_scores_are_rounded": [str(value) for value in alternative],
            "alternative_unrounded_scores": [str(value) for value in alternative_scores],
            "component_normalizations_recovered": False,
        },
        "decision_vectors": decisions,
        "coupling_under_declared_convention": coupling,
        "criticality_weight_sum_only": str(criticality_sum),
        "cohesion_recalculated": False,
        "survey_aggregate_checks": survey,
        "expert_normalized_indices": expert_indices,
        "raw_responses_ratings_or_test_logs_generated": False,
        "original_R_script": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path, help="The corrected thesis Word file.")
    args = parser.parse_args()
    try:
        report = audit(args.document)
    except (ValueError, FileNotFoundError, KeyError, BadZipFile, ET.ParseError) as error:
        print("Aggregate verification failed: " + str(error), file=sys.stderr)
        return 1
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
