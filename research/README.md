# Lokale bibliotheek voor het MDM-onderzoek

Open **[index.html](index.html)** om op titel, auteur, bron-ID of thema te zoeken en de lokale PDF's en teksten te openen. De index werkt zonder server of internet. Externe bronlinks en eventueel actieve onderdelen van oorspronkelijke webpagina's kunnen wel internet gebruiken; de afgeleide `.txt`-bestanden zijn volledig lokaal leesbaar.

## Inhoud en status

- `corpus/books/`: openbare boekteksten, officiële proefhoofdstukken en boekinformatie.
- `corpus/papers/`: papers, auteursmanuscripten, preprints en publicatiepagina's.
- `corpus/standards/`: standaarden, officiële documentatie, beleidsadviezen en cataloguspagina's.
- `corpus/professional/`: herkenbaar gescheiden leveranciersliteratuur.
- `corpus/methods/`: documenten over reviewmethodologie en gelinkte achtergrondbronnen.
- `corpus/text/`: automatisch geëxtraheerde tekst voor lokaal zoeken.
- `corpus/access-responses/`: technische responses/andere bestanden die geen inhoudelijk brondocument vormen.
- `evidence/sources.csv`: bibliografisch bronregister, selectiestatus en lokale bestanden.
- `evidence/artifacts.csv`: bestandsidentiteit, herkomst, eerste tekst en reviewstatus.
- `evidence/downloads.csv`: alle downloadroutes, inclusief fouten, redirects en hashes.
- `evidence/access-register.csv`: mislukte, onvolledige en niet-inhoudelijke downloadroutes.
- `evidence/duplicates.csv`: identieke bytes onder verschillende routes of bron-ID's.
- `evidence/legacy/`: ongewijzigde kopieën van eerdere matrices en ontwerpclaims.

De laatste telling staat in `evidence/download-summary.json`. Bestandsaantallen zijn geen aantallen onafhankelijke studies. Twee bron-ID's kunnen hetzelfde werk aanduiden; een bron kan meerdere versies, bijlagen of verwijzingen hebben.

Een PDF is niet automatisch een volledige publicatie. De index maakt onder meer onderscheid tussen excerpts, auteursversies en gelinkte kandidaten. Voor `linked_pdf_candidate_not_yet_screened` is de oorspronkelijke bron-ID de ontdekkingsroute, niet de bibliografische identiteit van het gelinkte document. Formele selectie, passageanalyse en onafhankelijke bronbeoordeling volgen nog.

Volledige commerciële boeken en normteksten zijn niet verworven via betaalmuur- of toegangscontroleomzeiling. Een officieel abstract, een proefhoofdstuk of een cataloguspagina is geen vervanging van de volledige tekst. Een HTTP-fout bewijst niet dat het document nergens openbaar beschikbaar is.

## Nieuwe onderzoeksrichting

De actieve opdracht staat in [RESEARCH-BRIEF.md](RESEARCH-BRIEF.md), het werkprotocol in [research-protocol.md](research-protocol.md) en de uitgevoerde verkenningen in [search-strategy.md](search-strategy.md). De studie is beschrijvend en synthetiserend; het prototype is volledig buiten scope. De oudere paper in de projectroot blijft een herkenbare eerdere baseline.

De nieuwe `claims-register.csv`, `concepts.csv` en `gaps.csv` hebben voorlopig alleen een schema. Zij zijn bewust niet gevuld met niet-uitgevoerde extracties of oude ontwerpclaims. De literatuur- en standaardenmatrix bevatten legacy-metadata plus nieuwe kandidaten; inhoudelijke herscreening staat nog open.

## Onderhoud

Vanuit de projectroot:

```bash
python research/scripts/collect_corpus.py
python research/scripts/build_catalog.py
```

De collector gebruikt de oude bronroutes en `evidence/download-seeds.csv`; hij hergebruikt geslaagde downloads en probeert overige routes opnieuw. Pas op met mutable webpagina's: een hergebruikte snapshot is geen nieuwe actualiteitscontrole. De indexgenerator controleert bestandshashes en maakt tekstextracties; hij voert geen inhoudelijke review uit.

`seed_expansion.py` legt de initiële aanvullende bronselectie vast en overschrijft bij uitvoering de seed- en kandidaatbestanden. Bewerk of voer dit bestand niet achteloos opnieuw uit na handmatige uitbreiding. De gegenereerde matrices bevatten de startregistratie: vóór inhoudelijke extracties moet de generator worden aangepast zodat beoordeelde cellen behouden blijven.

Zoek bijvoorbeeld lokaal met `rg -i 'survivorship|golden record' research/corpus/text/`. Tekstextractie kan fouten bevatten; controleer citaten altijd tegen het oorspronkelijke document. Deze collectie is voor lokale onderzoeksraadpleging; een download geeft niet automatisch toestemming voor herpublicatie van volledige teksten.
