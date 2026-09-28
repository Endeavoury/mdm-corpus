# Pre-evaluation research state

Het manuscript is een herzien ontwerpvoorstel, geen afgeronde empirische DSR-studie. Het prototype is niet formeel getest. De gerichte review is uitgevoerd door dezelfde AI-assistent; externe onafhankelijke beoordeling ontbreekt.

## Centrale these en theoretische propositions

**T:** expliciete contextbinding kan voor een vooraf afgebakende verzameling identiteit-, tijd- en gezagstaken praktisch relevante nettowaarde bieden boven dezelfde informatie in een conventioneel contextregister. T verlangt geen centrale opslag, RDF-database of OntoUML.

| Propositie | Verwacht mechanisme | Ondersteunende rationale, geen effectbewijs | Tegenbewijs voor de operationele claim |
|---|---|---|---|
| TP1 | Getypeerde contextverbindingen verbeteren selectie en interpretatie van relevante bronnen. | ISO/IEC 11179, PROV-O en kennisgraafliteratuur. | Geen vooraf relevant voordeel boven A1 met voldoende precisie, of slechtere prestaties/kosten. |
| TP2 | Betrouwbare epistemische metadata beperken onterechte opwaardering naar gezaghebbende informatie. | PROV-O en stelselverantwoordelijkheden; samengestelde classificatie is eigen voorstel. | Geen relevante foutreductie, meer gezagsfouten of blind vertrouwen in misleidende labels. |
| TP3 | Ontologische verdieping helpt bij specifieke identiteit-/rolproblemen. | UFO/OntoUML en OntoClean als analysekandidaten. | Gelijke detectie, meer fout-positieven of disproportionele analyse-/onderhoudstijd. |
| TP4 | Versieafhankelijkheden ondersteunen historische reconstructie en wijzigingsanalyse. | Temporele databaseliteratuur, provenance en versieerbare metadata. | Een eenvoudiger versiearchief is praktisch gelijkwaardig of beter; mappings/resolutie veroorzaken extra fouten. |

De propositions worden vóór uitvoering geconcretiseerd met populaties en relevante marges. Een negatieve uitkomst mag niet achteraf worden ontweken door de betekenis van “kan” of “voldoende” te veranderen. Een breed onzekerheidsinterval is onbeslist, niet automatisch weerlegging of ondersteuning.

## Afgeleide design principles

- DP1: onderscheid representatierollen en documenteer mappings; resource-disjunctie is niet universeel vereist.
- DP2: bind gezagsclaims aan uitspraken en bronnen.
- DP3: onderscheid referentidentiteit, record, versie en document.
- DP4: modelleer geldigheid en registratiekennis afzonderlijk.
- DP5: scheid inferentie, graafvalidatie en feitelijke kwaliteitsbeoordeling.
- DP6: publiceer een doel- en versiegebonden productcontract; onderzoek hergebruik van bestaande profielen.
- DP7: beheer verandering, terugmelding en verantwoordelijke besluiten.
- DP8: pas ontologische verdieping alleen toe bij een gemotiveerde behoefte en aanvaardbare kosten.
- DP9: maak uitspraaksoort, registratiehandeling, productiemethode, onzekerheid, gezagsgrond en bewijsstatus afzonderlijk zichtbaar.

Dit zijn kandidaatprincipes. Bronpassage, extra aanname, alternatief, requirement en experiment zijn verbonden in `derivation-register.csv` en de paperbijlage. Geen principe is empirisch gevalideerd.

## Nog te onderzoeken prototype-eigenschappen

Alle eigenschappen hebben status **niet beoordeeld**: roltypering; data-elementkoppelingen; identifier-scope/resolutie; bron- en gezagsregistratie; geschiedenis en correcties; context per bewering; regel-/modelversies; kwaliteitsvalidatie; mappings; lifecycle; productmanifest; interfaces; events/terugmelding; toepasselijkheid; en consumptie door mens, applicatie en AI. Ook repository/release, configuratie en feitelijke implementatie moeten nog worden geïnventariseerd. Ontbrekende documentatie in deze repository bewijst niet dat een functie ontbreekt.

## Benodigde experimenten en variabelen

| Experiment | Onafhankelijke variabelen | Primaire afhankelijke variabelen | Belangrijke controles |
|---|---|---|---|
| E1 | A0 technisch; A1 conventioneel contextregister; B1 expliciete binding. | Correcte én herleidbare antwoorden; B1−A1. | Gelijke broninhoud, toegang, training en antwoordbudget; taaktype en expertise. |
| E2 | Annotatievorm × betrouwbare/ontbrekende/misleidende annotatie. | Onterechte gezagsopwaarderingen; passende en onnodige onthouding. | Gelijk bewijs per kwaliteitsconditie; mens en AI afzonderlijk; model-/promptversie vastgezet. |
| E3 | Modelreview zonder/met gerichte ontologische verdieping. | Juist gedetecteerde fouten, fout-positieven en analistentijd. | Gelijke expertise, taakset en beschikbare domeininformatie. |
| E4 | Zelfde versiearchief zonder/met afhankelijkheden × intacte/verstoorde contextresolutie. | Historische correctheid, impactdetectie, hersteltijd en kosten. | Dezelfde bronhistorie; verouderde mappings en ingetrokken toegang als negatieve scenario’s. |

M01–M23 ondersteunen component- en contracttoetsen. Een hogere metadatadekking mag niet als vergelijkend bewijs voor T worden gebruikt. De primaire consumentuitkomsten worden onafhankelijk geadjudiceerd. Behandelingsafhankelijke mislukkingen blijven in de noemer.

## Beslisregels voor ondersteuning en falsificatie

De primaire operationele hypothese vereist een E1-verbetering groter dan de vooraf vastgelegde minimaal relevante winst δQ, binnen de toegestane kritieke fouttoename η en extra beheerlast κ. Deze grenzen zijn **nog niet vastgesteld** en mogen niet uit de uitkomsten worden gekozen.

Een onzekerheidsinterval geheel boven δQ, samen met het halen van de fout- en kostengrenzen, ondersteunt de afgebakende claim. Een bovengrens onder δQ weerspreekt praktisch relevante winst. Praktische gelijkwaardigheid van A1 en B1 bij hogere B1-kosten weerspreekt de nettowaarde/noodzaak van de rijkere oplossing. Een negatief effect is sterker tegenbewijs. Een secundaire AI- of ontologiewinst redt een gefaalde primaire hypothese niet achteraf.

## Startvoorwaarden die nog ontbreken

Volledige toepasselijke normteksten; externe construct- en bronreview; een onderbouwde casus met minimaal twee onafhankelijk beheerde registraties vóór een meerregistratieclaim; prototype-inventarisatie; een onafhankelijke gouden standaard; steekproefonderbouwing; definitieve interventies; en preregistratie van marges, uitkomsten en analyse. Twee registraties zijn een minimale startvoorwaarde, geen bewijs van Stelselbrede representativiteit.

Het huidige resultaat is een beter afgebakend en falsifieerbaar onderzoeksvoorstel. De theoretische en empirische waarheid van de centrale these blijft open.
