# Thèse de doctorat / PhD Thesis

Ce dépôt public héberge les versions Word de la thèse, le PDF de référence de l'édition française de 285 pages et un outil de contrôle des agrégats publiés.

## MAB-FRENCH-4 — Clarifications scientifiques A, B et C

**[Télécharger le Word corrigé (.docx, environ 38,3 Mo)](https://raw.githubusercontent.com/jacobngb/phd-thesis-formatted/main/MAB_FRENCH_4_Corrections_Scientifiques_ABC.docx)**

Cette édition prolonge MAB-FRENCH-3 par des corrections ciblées du formalisme, du statut des expérimentations et de la traçabilité des données. Les expressions manquantes n'ayant pas été retrouvées dans les sources disponibles, les compléments distinguent **relations déductibles**, **conventions proposées** et **paramètres historiques non documentés**. La proposition d'existence d'une partition optimale est explicitement conditionnelle ; elle ne démontre pas l'optimalité empirique du prototype.

Le total des quinze poids du tableau 2.8 est corrigé de **18 à 19**, sans modifier les poids individuels ni les résultats rapportés. Sous une agrégation linéaire commune, les poids **0.40, 0.30, 0.20 et 0.10** reproduisent les scores de granularité affichés. Leur reconstruction n'est pas une preuve des paramètres historiques : les arrondis permettent d'autres pondérations compatibles. Les normalisations des scores de décision, les ratios de couplage, les pourcentages du questionnaire et les indices des experts sont explicités.

La méthodologie distingue les essais fonctionnels et HTTP rapportés, les résultats modélisés et les tests événementiels, de panne, de compensation et de convergence restant à réaliser ou à documenter directement. La matrice C.3 est réalignée sur les objectifs de l'introduction. L'annexe **C.4** présente les déductions, leurs hypothèses et les pièces nécessaires à un audit complet. Les pourcentages des experts désignent des indices du maximum de l'échelle, **pas des taux d'approbation**.

**Aucune réponse individuelle, note d'expert, transcription ou trace d'essai manquante n'a été inventée.** La matrice d'enquête, les formulaires remplis, les règles d'agrégation et les journaux originaux restent nécessaires pour authentifier les résultats ; leur absence ne peut être compensée par un simple contrôle des agrégats.

Les **72 images**, leurs dimensions et leurs recadrages sont conservés sans compression supplémentaire. Les **41 objets mathématiques d'origine** et les douze blocs de code sont inchangés ; dix expressions mathématiques modifiables sont ajoutées avec leur statut explicite. Les valeurs d'enquête, les moyennes d'experts et les mesures du prototype sont préservées. Le texte reste en **13 points et interligne 1,5**, hors tableaux, formules et algorithmes.

Le rendu de référence compte **326 pages**, sans page blanche. Les **323 renvois de pagination** du sommaire et des listes sont actualisés, avec une table des matières limitée à trois niveaux. La pagination du Word peut varier selon le logiciel et les polices disponibles. Les éditions antérieures restent accessibles.

### Contrôle reproductible des agrégats

**[Télécharger le script de contrôle (.py)](https://raw.githubusercontent.com/jacobngb/phd-thesis-formatted/main/verifier_agregats_abc.py)**

Avec Python 3.9 ou ultérieur, sans dépendance externe, placer le script et le Word dans le même dossier puis exécuter :

```bash
python3 verifier_agregats_abc.py MAB_FRENCH_4_Corrections_Scientifiques_ABC.docx
```

Le script lit les tableaux du Word et produit un rapport JSON de contrôle arithmétique, avec les hypothèses de reconstruction et les limites d'identification. **Ce nouvel outil n'est pas le script R original de l'enquête**, ne reconstitue pas les données individuelles et n'exécute aucun test du prototype.

## MAB-FRENCH-3 — Revue de la littérature et harmonisation

**[Télécharger le Word harmonisé (.docx, environ 38,3 Mo)](https://raw.githubusercontent.com/jacobngb/phd-thesis-formatted/main/MAB_FRENCH_3_Revue_Litterature_Harmonisee.docx)**

Cette édition reprend le nouveau manuscrit fourni, avec son chapitre de revue de la littérature traduit en français. La thèse comprend désormais **cinq chapitres**. La subdivision du travail, les titres et les renvois sont réadaptés ; la synthèse des travaux antérieurs et la conclusion générale sont alignées sur la lacune scientifique et de conception de la section **0.2.2**, dont le texte est préservé. Les titres originaux des travaux cités sont conservés pour faciliter leur identification bibliographique.

Le texte est en **13 points et interligne 1,5**, y compris le sommaire, les légendes, la bibliographie et la prose des annexes. Les tableaux, les formules et les algorithmes conservent leur présentation adaptée. La table des matières s'arrête à trois niveaux ; les **321 références de pagination** du sommaire et des listes sont actualisées.

Les **72 images** conservent leurs fichiers originaux, leurs dimensions d'affichage et leurs recadrages, sans compression supplémentaire. Les diagrammes du nouveau chapitre 1 restent **en anglais**. Les **41 objets mathématiques**, les données des **75 tableaux** et les douze blocs de code sont préservés ; seuls les numéros d'équation et les renvois nécessaires ont été harmonisés.

Le rendu de référence compte **320 pages**, sans page blanche, avec une pagination préliminaire romaine puis arabe pour le corps du travail. Les grands diagrammes restent entiers, et les noms des interfaces sont regroupés avec leurs adresses pour éviter des captures isolées. La pagination du Word peut varier selon le logiciel et les polices disponibles.

Les doublons de numérotation et les renvois à des tableaux ou à un chapitre absents ont été corrigés sans inventer de contenu. Les notices doctorales manquantes et les informations d'actualité nécessitant des sources primaires sont signalées dans les commentaires Word. Les éditions antérieures restent disponibles ci-dessous.

## MAB-FRENCH-2 — Pagination professionnelle et interligne 1,5

**[Télécharger le Word mis en page (.docx, environ 38,1 Mo)](https://raw.githubusercontent.com/jacobngb/phd-thesis-formatted/main/MAB_FRENCH_2_Pagination_Professionnelle.docx)**

Le texte courant et la bibliographie sont en **interligne 1,5**. Les tableaux, les formules, les présentations statistiques et les annexes conservent des espacements adaptés. Les paragraphes vides et les sauts inutiles ont été supprimés ; l'ouverture du chapitre 1 n'est plus isolée. Les légendes restent avec leurs figures, et les douze blocs de code des annexes tiennent chacun sur une seule page.

Cette édition reprend les corrections de renvois précédentes, sans réécrire le contenu scientifique ni modifier les données des **75 tableaux**, les **41 objets mathématiques** ou les **70 illustrations**. Les fichiers des illustrations, leurs dimensions et leurs recadrages sont conservés à l'identique, sans compression supplémentaire. Les **315 renvois de pagination** du sommaire et des listes sont actualisés ; l'annexe E figure désormais au sommaire.

La dédicace, les remerciements et le résumé français étaient sans texte dans le fichier fourni : leurs pages réservées et leurs entrées du sommaire ont été retirées, sans inventer de contenu. Un commentaire Word explique ce retrait ; les cinq remarques de contrôle des renvois restent disponibles.

Le rendu de référence compte **297 pages**, sans page blanche. Les espaces nécessaires aux grands diagrammes et aux changements de chapitre ou d'orientation sont préservés. La pagination du Word peut varier selon le logiciel et les polices disponibles. Cette édition avec interligne 1,5 est distincte de l'édition compacte de 290 pages ; les versions antérieures ne sont pas remplacées.

## MAB-FRENCH-1 — Renvois aux figures et tableaux corrigés

**[Télécharger le Word corrigé (.docx, environ 38,1 Mo)](https://raw.githubusercontent.com/jacobngb/phd-thesis-formatted/main/MAB_FRENCH_1_Renvois_Corriges.docx)**

Cette copie intègre **29 corrections de renvois**, notamment vers la figure 1.12 et le tableau 2.4, sans modifier les formules, les statistiques ni les images. Les numéros de page du sommaire et des listes ont été actualisés. Cinq commentaires Word signalent trois renvois sans tableau identifiable et deux doublons de numérotation à valider.

Le rendu de contrôle compte **300 pages**. La pagination du Word peut varier selon le logiciel et les polices disponibles. Les éditions antérieures restent disponibles ci-dessous.

## Version française académique — 290 pages

**[Télécharger la version française de 290 pages (.docx, environ 33,5 Mo)](https://raw.githubusercontent.com/jacobngb/phd-thesis-formatted/main/These_Francaise_Academique_290_pages.docx)**

Cette version est allégée sans réécriture du texte. L'introduction, le chapitre 1, les formalismes mathématiques et les statistiques sont préservés. La table des matières est limitée aux trois niveaux **1, 1.1 et 1.1.1**. Le PDF de contrôle compte **290 pages au total, dont 19 pages d'annexes**.

Le Word reste modifiable ; sa pagination peut varier selon le logiciel, les polices disponibles et les paramètres d'impression. Les autres éditions ci-dessous restent disponibles séparément.

## Version française académique — 285 pages

**[Télécharger la version française de 285 pages (.docx, environ 33,5 Mo)](https://raw.githubusercontent.com/jacobngb/phd-thesis-formatted/main/These_Francaise_285_Pages.docx)**

**[Télécharger le PDF de référence à pagination fixe (.pdf, environ 12,4 Mo)](https://raw.githubusercontent.com/jacobngb/phd-thesis-formatted/main/These_Francaise_285_Pages.pdf)**

Cette édition compte **285 pages au total, pages préliminaires comprises, dont 11 pages d'annexes**. Les annexes occupent les pages physiques 275 à 285, numérotées 257 à 267 dans le corps du document. La table des matières est limitée aux trois niveaux **1, 1.1 et 1.1.1** ; les titres de niveau inférieur restent présents dans le texte.

La réduction de 315 à 285 pages repose uniquement sur la mise en page : suppression de paragraphes vides et de sauts de page inutiles, ajustement des espacements et optimisation des tableaux des annexes, toujours en taille 11. **Aucun texte du manuscrit n'a été supprimé ni paraphrasé. L'introduction et le chapitre 1 sont conservés intégralement, y compris leur mise en forme ; les formalismes mathématiques, les statistiques et les graphiques restent inchangés.**

Le PDF fixe la pagination à 285 pages. Le Word reste modifiable ; sa pagination peut varier selon le logiciel, les polices disponibles et les paramètres d'impression.

Cette version traduit le manuscrit corrigé récemment fourni. Elle comprend la page de titre, la dédicace, les remerciements, le résumé, l'abstract, la table des matières, la liste des sigles et abréviations, les listes des figures et des tableaux, ainsi que le corps de la thèse, les références et les annexes.

Les données, les équations et les graphiques d'origine sont préservés. Les graphiques en anglais n'ont pas été traduits ; les quelques schémas déjà en français dans la source restent inchangés. Les tableaux de données sont composés en taille 11. La pagination des pages préliminaires est en chiffres romains et celle du corps de la thèse en chiffres arabes.

La dédicace et les remerciements sont des propositions à personnaliser, car les documents sources n'en contenaient pas. Le résumé et l'abstract ont été rédigés à partir du manuscrit. Le fond et la numérotation d'origine sont conservés, sans réécriture des éventuelles incohérences de fond ou de renvoi.

L'[édition française antérieure de 315 pages](https://raw.githubusercontent.com/jacobngb/phd-thesis-formatted/main/These_Francaise_Academique_Complete.docx) reste disponible séparément.

## Version anglaise complète / Complete English version

**[Télécharger la version anglaise complète / Download the complete English thesis (.docx, approximately 33.4 MB)](https://raw.githubusercontent.com/jacobngb/phd-thesis-formatted/main/PhD_Thesis_Formatted.docx)**

The English version now includes the title page, dedication, acknowledgements, English abstract, French résumé, keywords, table of contents, abbreviation and acronym glossary, list of figures and list of tables. The contents stop at three heading levels: **1, 1.1 and 1.1.1**. Preliminary pages use Roman numerals; the body starts at Arabic page 1.

This English file is based on the newly supplied `SEMICOPY_Corrected_Numbered-1.docx`, which contains the same corrected manuscript used for the French edition. Its general introduction, existing chapter structure, research content, references, appendices, original graphics and equations are preserved. Table text is formatted at 11 points. This current-manuscript edition replaces the earlier reorganised English download.

The dedication and acknowledgements are proposed texts to personalise, since no originals were supplied. The abstract and résumé summarise the corrected manuscript's reported evidence.

## Télécharger sur téléphone / Download on a phone

Touchez le lien du fichier souhaité. Si le navigateur affiche un aperçu, ouvrez son menu et choisissez **Télécharger** ou **Enregistrer**. Le fichier peut ensuite être ouvert dans Microsoft Word.

Tap the desired file link. If a preview opens, use the browser menu and choose **Download** or **Save**.
