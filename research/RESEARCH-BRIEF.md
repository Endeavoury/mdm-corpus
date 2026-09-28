# Actieve onderzoeksopdracht: brede MDM-review

Vastgelegd op 8 september 2026 op basis van de aanvullende gebruikersprompt. Dit document is een gestructureerde weergave van de opdracht, geen onderzoeksbevinding. De nieuwe opdracht vervangt voor deze fase de eerdere ontwerpgerichte SMDP-onderzoekslijn.

## Rol en doel

Voer academisch onderzoek uit op het snijvlak van Master Data Management, Data Management, Data Governance, Metadata Management, Data Quality, Semantic Interoperability, Information Modelling, Ontology Engineering, Enterprise Architecture, Data Products, Knowledge Representation en Nederlandse overheidsinformatievoorziening.

Het doel is kennisverzameling, synthese en structurering van de huidige wetenschappelijke, normatieve en professionele kennis over Master Data en Master Data Management. Ontwerp in deze fase geen nieuw MDM-product, nieuwe architectuur of nieuwe standaard.

**Het bestaande prototype staat volledig buiten scope.** Gebruik het niet om onderzoeksvragen te formuleren, bronnen te selecteren, eisen af te leiden, architectuurkeuzes te rechtvaardigen of conclusies te sturen.

Onderzoek definities, ontstaan en evolutie, theoretische perspectieven, organisatorische en technische problemen, capabilities, architectuurpatronen, governance, standaarden, metadata, semantiek, ontologie, nieuwe ontwikkelingen, controverses en kennishiaten.

## Onderzoekskarakter

Positioneer de studie als scoping review, state-of-the-art literature review, standards landscape analysis en conceptual synthesis. Gebruik waar passend principes uit systematische literatuurreviews. Forceer geen effectstudie of meta-analyse. Beschrijf de methode transparant en reproduceerbaar. Benoem gebruikte methodologische richtlijnen pas inhoudelijk na broncontrole; een verzameling downloads is geen afgeronde review.

## Hoofdvraag

“Wat is de huidige stand van wetenschappelijke, normatieve en professionele kennis over Master Data Management, en hoe hangen de belangrijkste concepten, capabilities, standaarden, architecturen en governancebenaderingen met elkaar samen?”

Deze vraag wordt gedurende protocolontwikkeling verfijnd zonder het prototype als uitgangspunt.

## Verplichte vraagthema's

1. Definities van Master Data in verschillende bronnen.
2. Onderscheid met transactionele data, reference data, metadata, analytical data, operational data, datasets en data products.
3. Businessproblemen die MDM probeert op te lossen.
4. Organisatorische capabilities.
5. Technische platformcapabilities.
6. Bestaande architectuurpatronen.
7. Registry, consolidation, coexistence, centralized/transactional en federated MDM.
8. Identifiers, entity resolution, matching, deduplicatie, survivorship, merge/split en hierarchy management.
9. Data Governance binnen MDM.
10. Data owner, data steward, custodian, domain owner en product owner; bronafhankelijke rolverschillen.
11. De rol van Data Quality.
12. Kwaliteit, validiteit, volledigheid, consistentie, actualiteit en juistheid.
13. Historie en temporaliteit.
14. Provenance en lineage.
15. Metadata en metadataregistries.
16. Relatie tussen MDM en semantiek.
17. Begrippen, definities, vocabularies, ontologieën, informatiemodellen, logische datamodellen en fysieke schemas.
18. Knowledge graphs en Semantic Web binnen MDM.
19. MDM en Data Products.
20. MDM, Data Mesh en federatieve data-architecturen.
21. Nieuwe behoeften door AI en AI-agents als afnemer; geen automatische vertaling van verwachting naar eis.
22. Kennishiaten in de MDM-literatuur.

## Broncategorieën

**Wetenschappelijke literatuur:** peer-reviewed werk over MDM, Master Data Governance, Enterprise Data Management, governance, kwaliteit, entity resolution, record linkage, reference data, metadata, interoperabiliteit, ontology engineering, knowledge graphs, data products, data mesh, data-centric architecture, semantic layers en AI met gestructureerde kennis. Zoek waar toegankelijk via Google Scholar, Crossref, ACM, IEEE, Springer, ScienceDirect, Wiley en AIS. arXiv alleen aanvullend; onderscheid preprints van gepubliceerde versies.

**Boeken:** DAMA-DMBOK en relevante fundamentele/professionele werken over MDM, Enterprise MDM, governance, kwaliteit, metadata, ontology engineering, Semantic Web, Data Products en Data Mesh. Een boek is niet automatisch peer-reviewed onderzoek. Registreer volledige tekst, proefhoofdstuk en cataloguspagina afzonderlijk.

**Internationale standaarden:** ISO 8000-serie, ISO/IEC 11179-serie, ISO 704, ISO/IEC 25012 en ISO 8601 waar relevant voor temporaliteit. Aanvullende normen alleen bij aantoonbare inhoudelijke aanleiding.

**Semantic Web:** RDF, RDFS, SKOS, OWL, SHACL, PROV-O, DQV, JSON-LD, SPARQL en OWL-Time. Beschrijf steeds doel én toepassingsgrens.

**Ontology engineering:** foundational ontologies, UFO, OntoUML, conceptual modelling en ontology-driven information modelling. OntoUML is geen Nederlandse overheidsstandaard.

**Nederlandse overheid:** MIM, NL-SBB, TOOI, NEN 3610, DCAT-AP-NL, BOMOS, NLGov REST API Design Rules, OpenAPI, Digikoppeling, FSC, NL GOV CloudEvents, MDTO indien relevant, Stelsel van Basisregistraties, de 12 eisen en Federatief Datastelsel. Controleer actuele versie en formele status uitsluitend bij officiële bronnen.

**Europa:** EIF, Interoperable Europe Act, SEMIC en Core Vocabularies, DCAT-AP en FAIR.

**Praktijkliteratuur:** architectuurpatronen, vendor-independent analyses, enterprise MDM, lessons learned en maturity models. Leveranciersmateriaal mag marktterminologie en productcapabilities illustreren, maar is nooit de enige wetenschappelijke onderbouwing.

## Conceptuele analyse

Analyseer afzonderlijk: term, begrip, definitie, concept, ontologische klasse, objecttype, attribuut, data-element, identifier, entiteit, record, master record, golden record, reference data, metadata, dataset en data product. Maak bronafhankelijke gelijkstellingen en verschillen expliciet; strijk ambiguïteit niet vooraf glad. De door de gebruiker gevraagde onderscheidingen zijn analysevragen, geen vooraf bewezen universele disjuncties. Onderzoek bijvoorbeeld of een auteur begrip en concept juist als synoniemen gebruikt.

Onderzoek of klassieke MDM-literatuur focust op data values, records, matching en golden records en hoe zij termen, definities, concepten, relaties, ontologieën en modellen behandelt. Neem niet vooraf aan dat expliciete semantiek in traditioneel MDM ontbreekt.

## Lifecycle en capability-taxonomie

Onderzoek identificeren → registreren → valideren → matchen → consolideren → verrijken → goedkeuren → publiceren → distribueren → wijzigen → historiseren → archiveren/verwijderen. Behandel dit als analysepad; stel niet vooraf dat iedere bron een identieke lineaire lifecycle voorschrijft. Registreer per fase verantwoordelijkheid, governance, metadata, kwaliteit en technische ondersteuning.

Kandidaat-capabilities om brononderbouwd te onderzoeken: Governance, Identity Management, Entity Resolution, Matching, Deduplication, Survivorship, Hierarchy Management, Reference Data, Data Quality, Business Rules, Metadata Management, Semantic Management, Data Modelling, Workflow, Approval, Versioning, History, Provenance, Lineage, Security, Access Control, Distribution, API Management, Eventing, Observability en Data Product Management.

Neem een capability pas als bevinding in de taxonomie op wanneer bronnen haar dragen. Maak organisatorische en technische capabilities onderscheidbaar.

## Architectuurpatronen

Breng bestaande registry-, consolidation-, coexistence-, centralized/transactional- en federatieve benaderingen in kaart. Vergelijk doel, voordelen, nadelen, governance, consistency model, ownership, latency, distributie, schaalbaarheid en semantische uitdagingen. Een in de literatuur beschreven patroon is geen aanbevolen ontwerp voor het prototype.

## Standaardenanalyse

Registreer naam, organisatie, jaar, versie, normatieve status, toepassing, abstractieniveau, constructen, relatie tot masterdata, metadata, data quality, semantiek, governance en technische interoperabiliteit, overlap, complementaire standaarden en beperkingen. Onderscheid documentstatus, Nederlandse lijststatus, toepassingsgebied en eventuele verplichting.

Gebruik waar inhoudelijk passend de categorieën TERMINOLOGY, SEMANTICS, ONTOLOGY, INFORMATION MODELLING, METADATA, MASTER DATA QUALITY, DATA QUALITY, PROVENANCE, DATA PRODUCT, GOVERNANCE, INTEROPERABILITY, API en EVENTING. Een document kan meerdere categorieën hebben.

## Nieuwe ontwikkelingen en AI

Analyseer Data Products, Data Mesh, knowledge graphs, semantic layers, federatieve datastelsels, API-first, event-driven architectures, data contracts, AI, AI agents, Retrieval-Augmented Generation en semantic grounding. Onderzoek of zij MDM vervangen, aanvullen of nieuwe behoeften creëren.

AI is één thema in de bredere review. Behandel definities, grounding, provenance, authoritative sources, structured knowledge, knowledge graphs, kwaliteit en traceability. Claim niet zonder bewijs dat semantiek of ontologie hallucinaties oplost.

## Registratie en integriteit

Werk in `research/corpus/`, `research/evidence/`, `research/analysis/` en `research/paper/`. Minimaal: `sources.csv`, `literature-matrix.csv`, `standards-matrix.csv`, `concepts.csv`, `claims-register.csv` en `gaps.csv` onder `research/evidence/`.

Registreer per bron ID, titel, auteur, jaar, type, publisher, DOI/URL, peer-reviewstatus, primair/secundair, onderzoeksdoel, methode, definities, bevindingen, beperkingen, MDM-relevantie, thema's en citatie. Onbekende velden blijven herkenbaar onbekend.

Classificeer conclusies als breed gedragen, meerdere bronnen, één bron, normatief, controversieel of eigen synthese. Registreer onderliggende bronnen en passage; consensus vergt inhoudelijke onderbouwing en kan niet uit een brongetal worden afgeleid.

Verzin geen bronnen, DOI's, auteurs, publicatiegegevens, standaarden, versies, citaten of resultaten. Controleer belangrijke claims primair. Benoem en analyseer tegenstrijdigheden zonder ongemotiveerd een bron te kiezen. Schrijf formeel academisch Nederlands. Gebruik voor de uiteindelijke paper LaTeX en BibLaTeX.

## Volgorde en uiteindelijke paper

Begin met (1) research protocol, (2) zoekstrategie, (3) corpus, (4) literatuurmatrix, (5) standaardenmatrix, (6) conceptanalyse en (7) voorlopige synthese. Schrijf geen paperhoofdstukken voordat voldoende corpusdekking is vastgesteld.

De uiteindelijke beschrijvende en synthetiserende paper behandelt: abstract; inleiding; methode; Master Data-definities; MDM-ontwikkeling; gerelateerde dataconcepten; capabilities; architectuurpatronen; identity/entity resolution; kwaliteit; governance/stewardship; metadata/data-elementen; semantiek/begrippen; ontologie/conceptual modelling; provenance/lineage/temporaliteit; standaardenlandschap; Nederlandse context; Data Products; federatieve architecturen; AI; synthese; research gaps; discussie; beperkingen; conclusie.

Een visualisatie die kennis ordent heet expliciet **synthesemodel van de literatuur**, niet gevalideerde nieuwe architectuur.
