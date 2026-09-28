# Voorgestelde paperstructuur

Werkdocument, 7 september 2026. Geen papertekst of onderzoeksresultaten. Uitgangspunt is hoofdvraag A in [research-design.md](research-design.md); de keuze is een onderzoeksvoorstel. Bronnen en bewijslimieten staan in de [standards matrix](standards-matrix.csv), [literature matrix](literature-matrix.csv) en het [claims-register](claims-register.csv).

Werktitel: **Designing a Semantic Master Data Product for Dutch Base Registries: Traceability across Meaning, Authority, Identity and Change**.

| Onderdeel | Argument en inhoud | Bewijs / nog benodigd resultaat |
|---|---|---|
| Abstract — als laatste schrijven | Probleem, methode, artefact, werkelijk gevonden effect, beperking | Geen verwachte effecten als resultaten presenteren |
| 1. Introduction | Praktisch probleem, maatschappelijke context, afgebakende gap, hoofdvraag en bijdrage | S25–S27; L05/L12; G01 nog toetsen; praktijkvoorbeelden verzamelen |
| 2. Research context and conceptual boundaries | Stelselcasus, begrippen en documentsoorten; authenticiteit tegenover juistheid | S08/S11/S13/S25/S49; registratiewet vastzetten |
| 3. Related work and theoretical foundations | MDM, governance, dataproducten, ontology engineering en interoperabiliteit | L05–L15; systematische review uitbreiden; concurrerende integraties |
| 4. Research methodology | DSRM, selectieprotocol, onafhankelijkheid prototype, evaluatie-episodes | L01–L04; screeninglog; vastgezette gold set |
| 5. Requirements and standards synthesis | Eisen, toepasselijkheid, aanvulling/overlap, conflicten, dekkingsgrenzen | S01–S50; R01–R22; volledige normpassages waar nodig |
| 6. Artifact design | Referentiemodel, mappings, identiteit/tijd/provenance, productcontract, governance | Nog te ontwerpen profiel en rationale; alternatieven vergelijken |
| 7. Demonstration | Afgebakende bron-tot-consumentketen met wijziging en terugmelding | Onafhankelijke casusdata; geen demonstratie als effectbewijs |
| 8. Evaluation | Baselines, gold set, meetmethode, effecten en foutgevallen | T01–T22; taak-/expertdata; negatieve uitkomsten |
| 9. Discussion | Welke mechanismen werken wanneer; complexiteit; overdraagbaarheid; threats | G01–G03 aan uitkomsten toetsen; DP1–DP8 herzien |
| 10. Conclusion | Alleen daadwerkelijk beantwoorde vraag en onderbouwde bijdrage | Geen universele architectuur-, standaard- of AI-claims |

## Beoogde tabellen en figuren

1. Begrippen- en abstractieniveautabel: term tot data product, met verboden gelijkstellingen.
2. Semantische keten als analysepad; expliciete mappingrelaties en alternatieve routes.
3. Compacte standaardsynthese; volledige matrix als bijlage.
4. Evidence → eis → principe → artefactonderdeel → evaluatietest.
5. Productcontract en afzonderlijke versies van semantische artefacten.
6. Tijdvoorbeeld: geldigheid, geregistreerde kennis, publicatie en notificatie.
7. Resultaten per baseline en ablatietest, inclusief foutzwaarte en kosten.

De eerste twee kunnen uit het huidige onderzoeksontwerp worden uitgewerkt. Figuren 4–7 mogen geen voltooide implementatie of evaluatie suggereren zolang die niet heeft plaatsgevonden.

## Bijlagen en reproduceerbaarheid

- Zoekprotocol met echte queries, exports, selectie- en uitsluitbesluiten.
- Standards- en literature matrix met exacte bronversies en toegangsniveau.
- Claims-register met onderscheid tussen bronfeit, afleiding en hypothese.
- Mappingprofiel met voorbeelden, tegenvoorbeelden en informatieverlies.
- Testspecificaties, geanonimiseerde/synthetische fixtures en gold set.
- Evaluatieprotocol, scorerubric, conflicten tussen beoordelaars en analysecode.
- Pas later: prototypeversie, aanpassingen en meetomgeving, gescheiden van de onafhankelijke eisenbasis.

## Argumentatiegrenzen

De integratiegap blijft voorlopig totdat eerder werk systematisch is vergeleken (G01). De referentiearchitectuur is een kandidaatoplossing, niet het logische gevolg van één norm. Het prototype is een mogelijke instantiatie; het bestaan ervan is geen wetenschappelijk bewijs. AI-resultaten gelden uitsluitend voor de onderzochte consument, taken, bronversies en meetcondities (G02). UFO/OntoUML krijgt alleen een positieve ontwerpaanbeveling als de analyse de extra inspanning rechtvaardigt (G03).

## Aanpassing bij hoofdvraag B of C

Bij B wordt de titel gericht op ontology-driven conceptual modelling; hoofdstukken 5–6 behandelen vooral identiteit, rollen en mappings naar MIM. De hoofdvergelijking is met/zonder ontologische analyse; dataproductmetadata en AI zijn context.

Bij C wordt de titel gericht op federatief lifecycle- en contractbeheer; hoofdstukken 5–6 behandelen bevoegdheid, versiecompatibiliteit, terugmelding en wijzigingsdistributie. De hoofdvergelijking meet verandering, herstel en afnemersinterpretatie. Een brede evaluatie van foundational ontologies vervalt dan als zelfstandig onderzoeksdoel.
