# Reviewer-response matrix

Beslissingen betreffen de 26 commentaren op de bewaarde ingediende versie. Acceptatie van een commentaar betekent geen afgeronde empirische validatie.

## RV01 — CRITICAL — geaccepteerd

**Commentaar:** De research gap is niet aangetoond

**Beoordeling:** De corpusgebonden lacune wordt eerlijk begrensd, maar selectiebias blijft de enige grond voor een wetenschappelijke lacune. De gerichte tegenzoekactie vindt Wang et al. (2009), SMDM, dat masterdata met een virtuele RDF-laag, ontologieën en queryverwerking verbindt. DPROD adresseert productbeschrijving. Gualo et al. (2023) adresseert masterdatakwaliteit. Daarmee valt de brede nieuwheidsclaim weg; onbekend is welk restprobleem na deze antecedenten overblijft.

**Wijziging:** Herformuleer de gap als nog onbeantwoorde vergelijkingsvraag over brongebonden identiteit, tijd en gezagsstatus onder semantische verandering. Maak bestaand werk en resterende onzekerheid expliciet.

**Rationale:** Een nieuw label of ontbrekende vermelding in een klein dossier bewijst geen nieuwe kennis. Een bewijsbare afwezigheidsclaim blijft buiten bereik.

**Gewijzigd:** sections/introduction.tex

**Status:** Afbakening en plan herzien; inhoudelijke/empirische open punten blijven expliciet

## RV02 — MAJOR — geaccepteerd

**Commentaar:** De bijdrage is vooralsnog een integratievoorstel

**Beoordeling:** Vijftien lagen, een tuple en een lijst normen leveren geen aangetoonde verklarende of prescriptieve theorie. De bijdrage kan routine engineering zijn. Er ontbreken een afgebakend mechanisme, toepassingscondities en uitkomsten waaronder dat mechanisme geen waarde toevoegt.

**Wijziging:** Formuleer vier conditionele propositions rond contextbinding, epistemische signalering, selectieve ontologische verdieping en versie-impact; onderscheid representatiecapaciteit van effect.

**Rationale:** Integratie kan een DSR-bijdrage worden, maar alleen wanneer de overdraagbare ontwerpkennis en haar grenzen worden getoetst.

**Gewijzigd:** sections/pre-evaluation.tex

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV03 — MAJOR — geaccepteerd

**Commentaar:** SMDP is onvoldoende discriminerend gedefinieerd

**Beoordeling:** De definitie telt wenselijke eigenschappen op. Vrijwel elke goed beheerde dataset plus catalogus kan eronder vallen. Niet helder is welke noodzakelijke voorwaarden een product tot masterdataproduct maken en welke semantische verplichtingen additioneel zijn.

**Wijziging:** Definieer een minimaal profiel met noodzakelijke en gezamenlijk voldoende voorwaarden binnen dit onderzoek; geef grensgevallen en leg vast dat een semantisch register zonder masterdata geen SMDP is.

**Rationale:** Een onderzoeksspecifieke classificatieregel is toegestaan, mits niet gepresenteerd als universele standaarddefinitie.

**Gewijzigd:** sections/theory.tex

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV04 — MAJOR — geaccepteerd

**Commentaar:** Masterdata en referentiedata zijn te summier afgebakend

**Beoordeling:** Entiteit versus record is bruikbaar, maar reference data krijgt slechts één zin. De rollen masterdata, referentiedata en metadata kunnen per context wisselen. Strikte scheiding op representatieniveau mag niet leiden tot een onhoudbare universele disjunctie.

**Wijziging:** Voeg operationele rolclassificatie toe, inclusief waardenlijst, conceptbeschrijving, transactiedatum en productmanifest als grensgevallen; registreer de rolcontext.

**Rationale:** De inhoudsrol, granulariteit en het publicatieobject zijn onafhankelijke dimensies.

**Gewijzigd:** sections/theory.tex

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV05 — MAJOR — geaccepteerd

**Commentaar:** De paper verbergt een echte terminologische spanning

**Beoordeling:** MIM 1.2 §1.6.1 beschrijft begrip als combinatie van term en definitie, terwijl de paper deze afzonderlijk modelleert. SKOS §3.5.1 laat bovendien een resource als SKOS-concept én OWL-klasse toe. De eigen scheiding is niet fout, maar volgt niet als universeel verbod uit deze standaarden.

**Wijziging:** Bespreek het MIM-woordgebruik en maak representatierollen expliciet; corrigeer de implicatie dat SKOS/OWL noodzakelijk disjunct zijn.

**Rationale:** Afzonderlijke beheerobjecten zijn een verdedigbare profielkeuze. Toegestane standaardpatronen blijven toegelaten als hun interpretatie traceerbaar is.

**Gewijzigd:** sections/theory.tex; sections/architecture.tex

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV06 — MAJOR — geaccepteerd

**Commentaar:** Van scope naar normatieve ontwerpverplichting is een te grote stap

**Beoordeling:** ISO 8000-110 behandelt uitwisselberichten met karakteristieke masterdata. ISO/IEC 11179-31 biedt registratiemetadata. Dat ondersteunt geen algemene plicht voor alle interne productgegevens of een bepaalde RDF-implementatie. De paper vermeldt beperkingen, maar het woord MOET in 23 eisen maskeert de inferentiesprong.

**Wijziging:** Classificeer iedere afleiding als bronconstraint, conditionele toepassing of eigen ontwerpkeuze; documenteer de aanvullende aanname en het toepasselijkheidsbesluit.

**Rationale:** Een normcatalogus kan scope ondersteunen; niet een ongelezen clausule of een causaal effect.

**Gewijzigd:** derivation-register.csv; sections/principles.tex

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV07 — MAJOR — geaccepteerd

**Commentaar:** Vijftien lagen zijn geen beargumenteerde noodzakelijke architectuur

**Beoordeling:** De lagen volgen vrijwel één-op-één de gevraagde onderwerpen. Functionele dekking is daarmee door constructie gegarandeerd, terwijl minimale realisatie, complexiteit en redundantie onbekend blijven. Ontologie, catalogus en dataproductmetadata kunnen grotendeels bestaande profielen hergebruiken.

**Wijziging:** Presenteer vijftien verantwoordelijkheden als views; definieer een minimale realisatie en optionele profielen. Vergelijk expliciet met een conventioneel register met dezelfde informatie.

**Rationale:** Dekking van onderwerpen bewijst geen optimale decompositie of noodzaak van afzonderlijke services.

**Gewijzigd:** sections/architecture.tex

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV08 — MINOR — gedeeltelijk

**Commentaar:** OntoUML is niet noodzakelijk gemaakt; dat is juist

**Beoordeling:** DP8 is terecht conditioneel. Noodzakelijkheid alsnog afdwingen zou de paper verzwakken. Wel ontbreekt een concreet besliscriterium wanneer de extra analyse zinvol kan zijn.

**Wijziging:** Behoud OntoUML als optionele analysemethode en voeg een probleemtrigger en stopregel toe; toets tegen dezelfde modelreview zonder foundational ontology.

**Rationale:** De suggestie dat OntoUML vereist moet zijn wordt verworpen; het verzoek om de keuze scherper te verantwoorden wordt overgenomen.

**Gewijzigd:** sections/principles.tex; sections/evaluation-design.tex

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV09 — MAJOR — geaccepteerd

**Commentaar:** Het formele metamodel is onvolledig

**Beoordeling:** E als verzameling triples identificeert geen twee gelijkluidende uitspraken van verschillende bronnen. N bevat geen literalwaarden. De typefunctie specificeert geen meervoudige typen. Context, tijdsintervallen en onvolledige informatie missen domeinen en uitkomstregels. Daardoor is het model nog niet voldoende voor reproduceerbare implementatie.

**Wijziging:** Geef edges/beweringen eigen identiteit, een incidentiefunctie naar nodes of literals, meervoudige typering, contextrecord en driestatus-validatie; beschrijf een synthetisch tegenvoorbeeld zonder uitvoering.

**Rationale:** Formele precisie is nodig juist waar conflicten en provenance worden geclaimd; dit blijft een partiële specificatie.

**Gewijzigd:** sections/architecture.tex

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV10 — MAJOR — geaccepteerd

**Commentaar:** Concrete cross-standard mappings ontbreken

**Beoordeling:** Relatienamen zoals formaliseert en modelleert zijn eigen termen. Er is nog geen adjudiceerbare mappingtabel die aangeeft welke standaardconstructies worden hergebruikt, waar extensions ontstaan en welk verlies optreedt.

**Wijziging:** Voeg kandidaatmappingtabel toe met richting, constructie, verlies, normatieve status en te beoordelen alternatief; hergebruik DPROD als vergelijking in C12.

**Rationale:** Een volledige nieuwe mappingstandaard is buiten deze fase; kandidaatregels en expliciete resterende beslissingen zijn wel mogelijk.

**Gewijzigd:** sections/integration-decisions.tex

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV11 — CRITICAL — geaccepteerd

**Commentaar:** Niet acceptabel als afgeronde DSR-evaluatiestudie

**Beoordeling:** Er is geen empirische evaluatie, externe probleemvalidatie of feitelijke prototype-inventarisatie. De paper claimt dat niet, maar de breedte en vorm kunnen toch de indruk van een voltooide DSR-bijdrage geven. DSR-methodologie noemen vervangt evaluatie niet.

**Wijziging:** Positioneer expliciet als pre-evaluation design proposal; benoem de uitgevoerde ontwerpactiviteiten en de nog niet uitgevoerde demonstratie/evaluatie.

**Rationale:** Afwijzing als afgeronde studie is gerechtvaardigd; evaluatieresultaten fabriceren is geen oplossing. Een voorsteltrack heeft andere criteria.

**Gewijzigd:** paper.tex; sections/introduction.tex

**Status:** Afbakening en plan herzien; inhoudelijke/empirische open punten blijven expliciet

## RV12 — MAJOR — geaccepteerd

**Commentaar:** De design principles zijn nog geen empirisch onderbouwde ontwerpwetten

**Beoordeling:** Broncitaten verklaren waarom onderwerpen relevant zijn, maar waarom juist deze normatieve oplossing optimaal is volgt niet. Sommige principes zijn generieke engineeringpraktijken.

**Wijziging:** Leg per principe probleem, bronpassage, extra aanname, alternatief, verwacht mechanisme, verliesconditie en toekomstige toets vast.

**Rationale:** De principes blijven afgeleide kandidaten; hun bestaande status wordt niet achteraf opgewaardeerd.

**Gewijzigd:** derivation-register.csv; sections/derivation-table.tex

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV13 — MAJOR — geaccepteerd

**Commentaar:** A/B identificeert het effect van semantiek niet

**Beoordeling:** Zelfs bij dezelfde feiten krijgt B extra structuur, retrievalhulp, provenance en constraints. Winst kan afkomstig zijn van documentatiekwaliteit, navigatie, meer ontwikkeltijd of een betere interface. Een gecombineerde ablatielijst maakt het pakket nog geen causale toets.

**Wijziging:** Gebruik A0 technisch, A1 conventioneel contextregister met dezelfde inhoud en B1 getypeerde verbindingen; houd toegang/presentatie waar mogelijk gelijk. Test ontologie en epistemische labels afzonderlijk.

**Rationale:** A0/B kan pakketwaarde meten; A1/B en gerichte manipulaties zijn nodig voor mechanistische claims.

**Gewijzigd:** sections/evaluation-design.tex

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV14 — MAJOR — geaccepteerd

**Commentaar:** Veel metrics meten naleving van de eigen definitie

**Beoordeling:** Semantic completeness, explainability en traceability dreigen tautologisch te worden: B bevat de velden die de metric telt, A niet. Metadatadekking is bovendien geen juistheid. Mappingrecall vereist een eindige, vooraf bepaalde kandidatenverzameling.

**Wijziging:** Scheid artefactconformiteit van consumentuitkomsten, definieer gouden standaard en denominatoren, meet fout-positieven, correcte onthouding en kosten apart.

**Rationale:** Een metadatacontrole blijft nuttig als formatieve toets, maar mag de comparatieve hoofdclaim niet dragen.

**Gewijzigd:** sections/case-evaluation.tex; derivation-register.csv

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV15 — MAJOR — geaccepteerd

**Commentaar:** De centrale these mist een praktische falsificatiegrens

**Beoordeling:** Een niet-significant verschil is niet automatisch tegenbewijs. H1 zegt slechts verhoogt, zonder minimaal relevant effect. H2 combineert winst en kosten zonder beslisregel. Daardoor kan elk klein voordeel worden gered als ondersteuning.

**Wijziging:** Leg estimands, vooraf te bepalen relevantie- en non-inferioriteitsmarges, onzekerheid en conditionele falsificatie vast. Onderscheid tegeneffect, verwaarloosbaar effect en onvoldoende informatie.

**Rationale:** Getalsdrempels zonder belanghebbenden of pilot verzinnen zou even onjuist zijn; de preregistratie krijgt een expliciete startvoorwaarde.

**Gewijzigd:** sections/evaluation-design.tex; sections/pre-evaluation.tex

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV16 — CRITICAL — geaccepteerd

**Commentaar:** BAG-fragment draagt geen Stelselbrede claim

**Beoordeling:** Er is niet eens een gevalideerd gekoppeld fragment met concrete definities en records, laat staan een vergelijking van meerdere registraties. Institutionele context is geen representatieve empirische casus.

**Wijziging:** Begrens conclusies tot ontwerp voor de context van het Stelsel; voeg een stage-gate toe die meerregistratieclaims blokkeert tot minimaal twee onafhankelijk beheerde registraties inhoudelijk en juridisch zijn onderbouwd.

**Rationale:** Representativiteit kan niet redactioneel worden gerepareerd; dit blijft open empirisch werk.

**Gewijzigd:** sections/case-evaluation.tex; sections/discussion.tex

**Status:** Afbakening en plan herzien; inhoudelijke/empirische open punten blijven expliciet

## RV17 — MINOR — geaccepteerd

**Commentaar:** Nederlandse standaardstatus is overwegend correct maar te indirect geciteerd

**Beoordeling:** De gecontroleerde lijstpagina’s bevestigen NL-SBB 1.0 pas-toe-of-leg-uit, MIM 1.2 aanbevolen, DCAT-AP-NL 3.0 in behandeling en OpenAPI lijstversie 3.0. Specificatieversie, procedurestatus en verplicht toepassingsgebied moeten afzonderlijk citeerbaar blijven.

**Wijziging:** Voeg een compacte status-/scopetabel met directe lijstbronnen toe; neem geen algemene wettelijke plicht of effectclaim over uit wervende bronbeschrijvingen.

**Rationale:** Er is geen reden een onjuistheid te verzinnen. Wel zijn procedurepagina’s veranderlijk en deels intern niet volledig bijgewerkt.

**Gewijzigd:** sections/integration-decisions.tex; source-audit.csv

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV18 — MAJOR — geaccepteerd

**Commentaar:** Epistemische annotatie mengt nog steeds verschillende dimensies

**Beoordeling:** Geregistreerd-zonder-afleiding staat naast deterministisch en AI. Ingevoerde waarden kunnen elders afgeleid zijn; AI is een techniekklasse, geen kansmodel. Authenticiteit is niet hetzelfde als waarschijnlijkheid of adjudiceerde waarheid.

**Wijziging:** Maak registratiehandeling, productiemethode, onzekerheidsmodel, gezagsgrond en bewijsstatus onafhankelijke velden. Registreer onbekend en betwist zonder opwaardering.

**Rationale:** Een veld dat AI heet maakt probabilistische zekerheid niet meetbaar; de combinatie blijft eigen onderzoeksprofiel.

**Gewijzigd:** sections/architecture.tex; claims-register.csv

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV19 — MAJOR — geaccepteerd

**Commentaar:** Metadata introduceren eigen beveiligings- en vertrouwensproblemen

**Beoordeling:** De evaluatie bespreekt niet systematisch misleidende provenance, ontoegankelijke bronnen, ingetrokken toegang, kwaadaardige context of uitlekken van informatie via identifiers en afleidingspaden. Dit zijn relevante aanvalsscenario’s, geen hier aangetoonde incidenten.

**Wijziging:** Voeg negatieve scenario’s en een toegangsfactor toe; scheid inhoudelijke bronclaims van vertrouwde instructies voor machineconsumenten. Toets onthouding bij ontoegankelijke context.

**Rationale:** Een compleet securityframework is buiten scope; negeren van deze effectmoderatoren is niet verdedigbaar.

**Gewijzigd:** sections/case-evaluation.tex; sections/discussion.tex

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV20 — MAJOR — geaccepteerd

**Commentaar:** Centrale semantisering kan pluraliteit en beheerbaarheid schaden

**Beoordeling:** Een centrale beschrijving kan één interpretatie institutioneel bevoordelen, legitieme verschillen uitwissen en wijzigingen tot knelpunten maken. Een federatieve graaf kan op zijn beurt afhankelijkheids- en beschikbaarheidsproblemen toevoegen. Het ontwerp kan slechter zijn dan lokale contracten.

**Wijziging:** Maak centralisatie onafhankelijk van semantische explicitering, behoud betwiste mappings en vergelijk beheerinspanning, wijzigingslatency en lokale autonomie.

**Rationale:** Dit zijn rivaliserende ontwerpverklaringen die negatief moeten kunnen uitpakken voor de gekozen architectuur.

**Gewijzigd:** sections/architecture.tex; sections/discussion.tex

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV21 — MINOR — geaccepteerd

**Commentaar:** Geen fictieve prototype-uitkomsten aangetroffen

**Beoordeling:** De paper scheidt toekomstige tests en bestaande bronbevindingen overwegend zorgvuldig. Het ontbreken van empirische resultaten is een inhoudelijke beperking, geen bewijs van misleiding.

**Wijziging:** Behoud die scheiding; vervang formuleringen die alleen administratieve dekking suggereren als bewijs door termen documentcontrole en ontwerpvoorstel.

**Rationale:** Een kritische review moet ook vaststellen welke gevreesde fout niet is gevonden.

**Gewijzigd:** sections/pre-evaluation.tex; traceability-audit.md

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV22 — MAJOR — geaccepteerd

**Commentaar:** Broncontrole is nog geen clausule- of interpretatieaudit

**Beoordeling:** De oorspronkelijke audit controleert sleutels en URL-herkomst. Dat bevestigt geen entailment, actualiteit of volledige dekking. ISO/NEN en verschillende artikelen blijven beperkt toegankelijk; sommige succesvolle HTTP-responses zijn slechts redirect- of scriptschermen.

**Wijziging:** Maak een claimniveau-bronaudit met access-status, geverifieerde passage, interpretatie, versie/scope en expliciete unresolved-vlag.

**Rationale:** HTTP 200, bestaande DOI en citaatsleutel zijn geen inhoudelijk bewijs.

**Gewijzigd:** source-audit.csv; source-audit.md

**Status:** Afbakening en plan herzien; inhoudelijke/empirische open punten blijven expliciet

## RV23 — MAJOR — geaccepteerd

**Commentaar:** Prototype-eigenschappen blijven volledig onbekend

**Beoordeling:** De paper inventariseert alleen de afwezigheid van implementatiegegevens in deze repository. Dat is correct, maar een reviewer kan geen uitvoerbaarheid beoordelen.

**Wijziging:** Leg een lijst benodigde prototype-evidence vast en koppel iedere eigenschap aan een geplande test; laat alle statusvelden op niet beoordeeld.

**Rationale:** Een echte inventarisatie kan zonder artefact niet worden uitgevoerd. Het open punt blijft zichtbaar in de response matrix.

**Gewijzigd:** sections/pre-evaluation.tex

**Status:** Afbakening en plan herzien; inhoudelijke/empirische open punten blijven expliciet

## RV24 — EDITORIAL — geaccepteerd

**Commentaar:** De standaardcatalogus verdringt de argumentatie

**Beoordeling:** De lange matrix en herhaalde disclaimers maken het 44-paginamanuscript eerder een dossier dan een gerichte paper. Er is veel herhaling tussen theorie, analyse en principes.

**Wijziging:** Verplaats de complete cross-standard tabel naar een appendix; laat in de hoofdtekst conflicten, kandidaatmappings en alternatiefselectie centraal staan.

**Rationale:** De uitgebreide dekking blijft reviewbaar; geen belangrijke scopegrens verwijderen om de paper korter te laten lijken.

**Gewijzigd:** sections/cross-standard-table.tex; paper.tex

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV25 — MAJOR — geaccepteerd

**Commentaar:** Traceability is administratief volledig maar semantisch dun

**Beoordeling:** Een rij met Sxx→Rxx→DPx→Cx→Mx bewijst niet dat de bron de requirement draagt. Veel requirements verbinden meerdere onafhankelijk te toetsen beweringen.

**Wijziging:** Behoud IDs maar voeg een derivation-register toe met bronlocatie, inference warrant, alternatief, tegenbewijs en experiment. Toon deze inferenties ook in de paper.

**Rationale:** Dit versterkt de controleerbaarheid zonder een niet-uitgevoerde inhoudelijke validatie te claimen.

**Gewijzigd:** derivation-register.csv; sections/derivation-table.tex

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

## RV26 — MINOR — geaccepteerd

**Commentaar:** Een gekozen referentieversie is niet noodzakelijk de nieuwste versie

**Beoordeling:** De paper is terecht versiegebonden. Actualiteitscontrole moet bevestigen wat op de gekozen pagina staat, niet automatisch overal de nieuwste release gebruiken. NL GOV CloudEvents vermeldt versie 1.1 maar heeft een linklabel 1.0; Digikoppeling gebruikt een redirectpagina.

**Wijziging:** Pin relevante publicaties; registreer pagina-inconsistenties en onvolledige toegang. Noem geselecteerde baselineversies en claim geen volledige release-monitoring.

**Rationale:** Het is methodisch beter onzekerheid te registreren dan tegenstrijdige metadata stilzwijgend glad te strijken.

**Gewijzigd:** source-audit.csv; references.bib

**Status:** Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd

