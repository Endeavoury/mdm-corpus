# Manuscript bouwen en controleren

De herziene paper gebruikt het gecontroleerde onderzoeksdossier, aangevuld met S51, L18 en L19 tijdens de kritische review. Het prototype is niet geëvalueerd.

## Bestanden

- `paper.tex` en `sections/`: volledige Nederlandstalige paper.
- `references.bib`: bibliografie uit de bestaande standards- en literature-matrices; bewijsbeperkingen blijven vermeld.
- `traceability-matrix.csv`: onderzoeksvraag → bron → requirement → principe → component → toekomstige metriek.
- `claims-register.csv`: bestaande claims met aanvullende expliciet gemarkeerde ontwerpafleidingen.
- `paper.pdf`: gecompileerd manuscript.
- `traceability-audit.md`: documentcontrole en resterende bewijsgrenzen.

## Compilatie

Vereist: Python 3 en Tectonic. Getest met Tectonic 0.17.0. Tectonic haalt bij eerste gebruik benodigde TeX-pakketten op; dit zijn bouwafhankelijkheden, geen onderzoeksbronnen.

```bash
make
```

Met een compiler buiten `PATH`:

```bash
make TECTONIC=/pad/naar/tectonic
```

Of afzonderlijk:

```bash
python scripts/prepare_paper.py
python review/finish_review_artifacts.py
tectonic -k --keep-logs paper.tex
python scripts/audit_paper.py
```

De voorbereiding genereert `references.bib` en drie LaTeX-tabellen opnieuw. Pas daarvoor de bestaande bronmatrices of expliciete ontwerpgegevens in `scripts/prepare_paper.py` aan. Bestaande claim-ID’s blijven behouden; het script voegt nieuwe ontwerpclaims alleen toe wanneer hun ID ontbreekt. Controleer wijzigingen inhoudelijk voordat een andere corpusversie wordt gebruikt.

`make audit` controleert het reeds gebouwde document. Het voert geen prototype- of AI-tests uit. De bibliografie gebruikt de consistente numerieke stijl `plainnat`. `AGENTS.md` is ongewijzigd gebleven.

## Review en revisie

De oorspronkelijke indieningsversie is bewaard in `review/baseline/submitted-manuscript.zip`. `peer-review.md` is vóór de revisie voltooid; de hash staat in `review/review-completed.json`. `reviewer-response-matrix.csv` scheidt acceptatie van commentaar van nog open empirisch werk. `source-audit.csv` beoordeelt claims inhoudelijk binnen de vermelde toegangslimieten. `pre-evaluation-research-state.md` beschrijft de nog niet uitgevoerde experimenten en falsificatie. De review is geen externe onafhankelijke beoordeling.

De eenmalige scripts `review/write_review.py`, `review/revise_sources.py` en `review/revise_manuscript.py` documenteren de revisiestappen en zijn geen buildcommando’s; voer ze niet opnieuw uit op de herziene tekst.
