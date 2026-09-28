# Nieuwe MDM-overzichtspaper

De nieuwe Nederlandstalige paper staat in **[mdm-overzicht.pdf](mdm-overzicht.pdf)**. Titel: *Master Data Management: concepten, capabilities en standaarden*. Dit is de eerste volledige manuscriptversie van de brede, beschrijvende literatuur- en standaardsynthese.

- [mdm-overzicht.tex](mdm-overzicht.tex): hoofddocument; hoofdstukken in `sections/`.
- [references.bib](references.bib): BibLaTeX-bibliografie met bron- en toegangsgrenzen.
- [traceability-audit.md](traceability-audit.md): documentcontrole en resterende beperkingen.
- [../evidence/claims-register.csv](../evidence/claims-register.csv): 68 analytische claims.
- [../evidence/paper-traceability.csv](../evidence/paper-traceability.csv): onderzoeksvraag → bron → passage → claim → papersectie.
- [../analysis/coverage-assessment.md](../analysis/coverage-assessment.md): gemotiveerde corpusafbakening.

Het prototype is niet gebruikt of geëvalueerd. De oudere ontwerpgerichte `../../paper.pdf` is een ander manuscript en is behouden.

## Bouwen

Vanaf de projectroot, met Python 3 en Tectonic 0.17.0:

```bash
python research/scripts/prepare_review_paper.py
python research/scripts/complete_review_analysis.py
tectonic -k --keep-logs research/paper/mdm-overzicht.tex
python research/scripts/audit_review_paper.py
```

Tectonic kan bij eerste gebruik TeX-pakketten downloaden. De paper gebruikt BibLaTeX met de BibTeX-backend; accenten worden in de bibliografie als TeX-escapes geschreven om byteproblemen te voorkomen. Een lokale compiler buiten PATH kan met zijn volledige pad worden aangeroepen.

De voorbereidingsscripts genereren tabellen en registraties opnieuw. Pas de brongegevens en expliciete analyses in die scripts samen met de tekst aan. `build_catalog.py` hoort bij de eerdere verwervingsfase en mag niet zonder aanpassing worden herhaald: het zou inhoudelijk verrijkte matrices door kandidaatregistraties vervangen.

De paper claimt geen volledige systematische review, geen onafhankelijke dubbele screening en geen effectvalidatie. Die grenzen zijn in het manuscript zichtbaar.
