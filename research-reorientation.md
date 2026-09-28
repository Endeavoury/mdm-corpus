# Heroriëntatie: corpus- en standaardenonderzoek

Datum: 8 september 2026. Status: voorstel voor een nieuwe onderzoeksrichting naar aanleiding van de wens om standaarden en corpusanalyse centraal te stellen. Geen uitgevoerde systematische review. Dit voorstel vervangt het bestaande manuscript en de bronregisters nog niet. De keuze tussen een integrerende analyse, een mappingstudie en een uitgebreidere DSR-opzet staat nog open.

## 1. Onderzoeksobject en bijdrage

Het primaire onderzoeksobject wordt het corpus van wetenschappelijke publicaties, standaarden, normen, specificaties, vocabularia en overheidskaders. De studie onderzoekt hun begrippen, toepasselijkheid, dekking en onderlinge relaties. Het Semantic Master Data Product is een mogelijke toepassing van de bevindingen; zijn noodzakelijkheid of meerwaarde vormt geen vooraf aangenomen uitgangspunt.

De beoogde bijdrage is een controleerbare cross-standard analyse met een begrippenkader, een dekkings- en relatiematrix en een onderbouwde onderzoeksagenda. Een integratieraamwerk kan een uitkomst zijn wanneer de analyse dat rechtvaardigt. Een concrete reference architecture en productevaluatie kunnen als afzonderlijk vervolgonderzoek worden behandeld.

Dit is een voorstel voor de taakverdeling tussen onderzoeksfasen, geen uitspraak dat een bepaalde reviewmethodologie al is toegepast of gevalideerd.

## 2. Werktitel en onderzoeksvragen

**Werktitel:** Semantische samenhang van masterdata in de Nederlandse overheid: een kritische analyse van literatuur, standaarden en interoperabiliteitskaders.

**Voorgestelde hoofdvraag:** Welke concepten, voorschriften en mechanismen biedt het geselecteerde nationale, Europese en internationale corpus voor het verbinden van betekenis, identiteit, gezag, historie en kwaliteit van masterdata in de Nederlandse overheid, en welke aansluitingen, spanningen en ongedekte behoeften worden daarin aantoonbaar zichtbaar?

Deelvragen:

1. Welke documenten behoren op basis van expliciete selectiecriteria tot het corpus, en wat zijn hun documentsoort, status, versie, toepassingsgebied en toegankelijke bewijsniveau?
2. Hoe definiëren de documenten term, concept, definitie, klasse, objecttype, data-element, entiteit, record, dataset, dienst en dataproduct, en welke overeenkomsten of verschillen zijn inhoudelijk onderbouwd?
3. Welke aspecten van identiteit, tijd, provenance, gezag, kwaliteit, governance, versiebeheer en distributie worden expliciet behandeld?
4. Welke onderlinge relaties zijn expliciet gespecificeerd, welke kunnen onder voorwaarden worden gemapt en welke blijven onderzoekersinterpretaties?
5. Welke schijnbare of werkelijke conflicten, redundantie en dekkingsgrenzen blijven bestaan na controle van abstractieniveau, toepassingsgebied en versie?
6. Welke integratievoorwaarden en vervolgvragen volgen uit deze analyse voor Nederlandse basisregistraties, zonder een specifieke implementatie vooraf te kiezen?

De studie hoeft niet te concluderen dat een nieuwe architectuur of standaard nodig is. Ook voldoende dekking door bestaande instrumenten, een toepassingsprobleem of onvoldoende beschikbare broninhoud zijn mogelijke uitkomsten.

## 3. Methode: eerst een protocol, dan een claim over systematiek

Het bestaande manuscript beschrijft een doelgerichte corpusselectie, zonder volledige reproduceerbare databasebrede screening. De huidige matrices bevatten 51 standaard-/kadervermeldingen en 19 literatuurvermeldingen. Deze vermeldingen zijn geen 70 onafhankelijke studies; onder meer profielen, documentdelen en verwijzingen naar dezelfde publicaties moeten worden onderscheiden. Zie `sections/introduction.tex`, onderdeel Bronbasis en syntheseprocedure.

Daarom wordt het bestaande dossier gebruikt als startcorpus, niet achteraf aangeduid als het resultaat van een afgeronde systematische review. De definitieve methodenaam en bijbehorende methodologische bronnen moeten worden gekozen en gecontroleerd vóór de nieuwe paper wordt geschreven.

### Corpusopbouw

Leg prospectief vast welke onderzoeksvraag, talen, periode, documenttypen en toepassingsgebieden worden meegenomen. Gebruik afzonderlijke selectieroutes voor academische literatuur en officiële standaarden/kaders. Registreer werkelijke zoekacties, zoeklocaties, zoekdatum, gevonden documenten, duplicaten, inclusie- en exclusieredenen en toegang tot de inhoud. Aanvullingen uit verwijzingen krijgen een herkenbare herkomst.

De eerdere lijst van gewenste standaarden is een startpunt dat selectiebias kan introduceren. Neem ook bronnen en bestaande integraties op die de noodzaak van het SMDP tegenspreken. Documenteer waarom een aanvullende standaard nodig is voor een concrete analysevraag. Behandel gelieerde profielen en versies als een documentfamilie waar dat dubbeltelling voorkomt.

### Analyse-eenheden en extractie

De analyse-eenheid is een concrete bronpassage over een begrip, relatie, voorschrift of mechanisme. Het document als geheel is de context van die passage. Maak per extractie minimaal zichtbaar:

| Veld | Vast te leggen informatie |
|---|---|
| Identificatie | Bron-ID, documentfamilie, versie en concrete paragraaf of stabiele locatie. |
| Documentrol | Normatief voorschrift, informatieve toelichting, conceptueel voorstel of empirische bevinding. |
| Inhoud | Begrip, relatie of mechanisme zoals de bron het beschrijft, met beperkte quote of controleerbare parafrase. |
| Reikwijdte | Toepasselijke objecten, doelgroep, omstandigheden en eventuele expliciete uitsluitingen. |
| Analytische code | Abstractieniveau, semantisch aspect en type relatie met aangrenzende bronnen. |
| Onderzoekersinterpretatie | Afzonderlijke mapping, aanname, onzekerheid en mogelijke alternatieve lezing. |
| Bewijsgrens | Volledige relevante tekst, gedeeltelijke tekst, abstract, catalogus of alleen bibliografie. |

Een catalogusvermelding kan editie en onderwerp ondersteunen, maar geen analyse van niet-ingeziene normclausules. Het ontbreken van toegang krijgt de code **niet beoordeelbaar**, niet **geen dekking**.

### Vergelijking en negatieve gevallen

Gebruik de volgende analytische categorieën als voorgesteld codeboek; hun bruikbaarheid moet tijdens een pilot worden beoordeeld:

- **Expliciete aansluiting:** de bron specificeert zelf een relatie of profielkoppeling.
- **Voorwaardelijke mapping:** een omzetting lijkt mogelijk, met vastgelegde aannames en mogelijk informatieverlies.
- **Aanvulling:** verschillende aspecten of abstractieniveaus worden behandeld.
- **Overlap:** vergelijkbare inhoud wordt behandeld; dit betekent nog geen overbodigheid.
- **Mogelijk conflict:** uitspraken lijken onder dezelfde omstandigheden onverenigbaar; scope en versie moeten eerst worden gecontroleerd.
- **Buiten toepassingsgebied:** het aspect is niet het doel van deze bron.
- **Niet gevonden in onderzochte passages:** een begrensde zoekuitkomst, geen universele afwezigheidsclaim.
- **Niet beoordeelbaar:** onvoldoende inhoudelijke toegang of onopgeloste interpretatie.

Een corpus-hiaat wordt alleen geclaimd ten opzichte van een expliciet gemotiveerde informatiebehoefte en een beschreven zoekdekking. Een ontbrekende passage in één document is geen wetenschappelijke research gap. Onderscheid documentatiehiaten, profiel-/mappinghiaten, implementatieproblemen en ontbrekend empirisch effectbewijs.

Laat een onafhankelijk beoordelaar een vooraf gekozen selectie van extracties en mappings controleren, waaronder alle zwaarwegende conflict- en hiaatclaims. Registreer verschillen en besluiten. Een administratieve traceability-audit vervangt deze inhoudelijke controle niet.

## 4. Rol van de basisregistraties

Het Stelsel fungeert primair als toepassingscontext voor de selectie en interpretatie van bronnen. Een beperkt BAG-voorbeeld kan aantonen hoe het analysecodeboek wordt toegepast op gedocumenteerde begrippen en modellen. Een analytisch voorbeeld toont niet aan dat een technische oplossing werkt of dat het volledige Stelsel is onderzocht.

Een volledige operationele keten en een prototype-experiment zijn in deze richting geen noodzakelijke deliverables van dezelfde paper. Wanneer de paper daadwerkelijk uitspraken over inhoudelijke relaties tussen registraties doet, blijven primaire bronnen en controle van die concrete relaties noodzakelijk. De eerdere minimale tweeregistratievoorwaarde hoorde bij een empirische meerregistratieclaim; zij is geen automatisch criterium voor iedere corpusstudie.

Verwacht casusresultaat: een brononderbouwde illustratie van enkele begrippen, representatieniveaus, mappings en resterende interpretatievragen. Geen volledige BRP–BAG–BRK–WOZ-integratie en geen productprestatiemeting.

## 5. Nieuwe paperstructuur

1. Inleiding: informatiebehoefte, toepassingscontext en afgebakende kennisvraag.
2. Begripsafbakening: masterdata, referentiedata, metadata, modellen en documentsoorten.
3. Onderzoeksmethode: corpusselectie, toegang, extractie, codeboek en kwaliteitscontrole.
4. Corpusprofiel: samenstelling, documentfamilies, versies, status en bewijsbeperkingen.
5. Conceptuele vergelijking: definities, eenheden, abstractieniveaus en ontologische aannames.
6. Cross-standard analyse: expliciete aansluitingen, mappings, overlap en mogelijke conflicten.
7. Dekking en hiaten: per gemotiveerde behoefte, met tegenbewijs en onzekerheid.
8. Nederlandse toepassingscontext: beperkte brononderbouwde illustratie.
9. Synthese: integratievoorwaarden en eventueel een analytisch integratieraamwerk.
10. Discussie: bijdrage, rivaliserende interpretaties, beperkingen en vervolgonderzoek.
11. Conclusie: uitsluitend bevindingen die de corpusanalyse daadwerkelijk draagt.

AI blijft een mogelijke afnemer en een analyseperspectief waar bronnen dat ondersteunen. Verwachte AI-prestatiewinst krijgt geen plaats als resultaat zonder effectonderzoek.

## 6. Migratie van het bestaande materiaal

| Bestaand materiaal | Gebruik in de nieuwe richting |
|---|---|
| Standards- en literature matrix | Startcorpus; selectie en inhoudelijke extractie opnieuw expliciet verantwoorden. |
| Claims-register en broncontrole | Behouden als auditspoor; nieuwe claims toevoegen met bestaande ID's intact. |
| Begripsafbakening en cross-standard analyse | Naar de kern van de resultaten, na passagecontrole. |
| Requirements en design principles | Herbeoordelen: expliciet bronvoorschrift, onderzoekersafleiding of ontwerpkeuze? Niet allemaal als corpusbevinding presenteren. |
| Vijftien architectuurlagen | Voorlopige sensitiserende analysecategorieën; open voor samenvoeging, aanvulling of verwerping. Geen voorgeschreven uitkomst. |
| Reference architecture en metamodel | Mogelijke ontwerpimplicatie of afzonderlijke vervolgpaper; niet het primaire onderzoeksobject. |
| Prototype en E1–E4 | Afzonderlijke latere ontwerp-/evaluatiefase. |
| Huidige presentatie | Concept bij de oude onderzoeksrichting; herzien na keuze van de nieuwe richting. |

De primaire traceability wordt **onderzoeksvraag → geselecteerde bron → passage → analytische code → vergelijkingsbevinding → integratievoorwaarde / open vraag**. Een aanvullende keten naar ontwerp en evaluatie kan later worden toegevoegd.

## 7. Eerstvolgende werkzaamheden

Na keuze van de richting: formuleer de definitieve hoofdvraag, leg corpusprotocol en codeboek vast, voer een beperkte extractiepilot uit en toets of de categorieën onderscheidend zijn. Registreer ontbrekende brontoegang en benodigde zoekuitbreidingen. Schrijf pas vervolgens de nieuwe methode- en resultatenhoofdstukken op basis van werkelijk uitgevoerde activiteiten.

Geen stappen van deze nieuwe protocoluitvoering worden met dit voorstel als voltooid geregistreerd. Het bestaande ontwerpgerichte manuscript blijft herkenbaar als eerdere onderzoeksbaseline.
