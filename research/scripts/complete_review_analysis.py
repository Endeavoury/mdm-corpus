"""Register the explicitly qualified conceptual synthesis in the overview paper."""
import csv
from pathlib import Path
E=Path(__file__).resolve().parents[1]/'evidence'
def read(n):return list(csv.DictReader((E/n).open(encoding='utf-8-sig',newline='')))
def write(n,rows):
 with (E/n).open(encoding='utf-8-sig',newline='') as f:fields=next(csv.reader(f))
 with (E/n).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
concept_data=[
('term','S11;S31','Aanduiding in een taal of begrippenstelsel','begrip; definitie','Labelgelijkheid bewijst geen conceptgelijkheid'),
('begrip','S11;S14','Afgebakende betekeniseenheid in een context','term; modelconstructie','Niet vooraf onderscheiden als andere universele categorie dan concept'),
('definitie','S11;S14','Beschrijving van begripsafbakening','dataschema','Definitiecriteria en veldrestricties hebben verschillende functies'),
('concept','S13;S31','Bronafhankelijke modelterm; SKOS-concept in begrippenstelsel','OWL-klasse; term','MIM- en SKOS-gebruik niet zonder analyse vereenzelvigen'),
('ontologische klasse','L08;S30','Categorie met formele of ontologische interpretatie','MIM-objecttype; SKOS-concept','SKOS verbiedt algemeen hergebruik als OWL-klasse niet'),
('objecttype','S13','Constructie binnen een informatiemodel','ontologische klasse; record','Ontologische commitment moet afzonderlijk worden onderzocht'),
('attribuut','S13;L20','Gemodelleerd kenmerk van een type of klasse','data-element; concrete waarde','Constructies verschillen per modelniveau'),
('data-element','S08','Geregistreerde dataspecificatie met conceptuele en representatieaspecten','attribuut; veldwaarde','Scopecontrole van norm; volledige clausuleanalyse ontbreekt'),
('identifier','S38;S39','Aanduiding binnen een identificatiecontext','entiteit; identiteit','Gelijke tekens zonder context leveren geen referentbewijs'),
('entiteit','L20;L21','Bedoelde referent van een gegevensbeschrijving','record','PROV-entity kan juist een informatieobject voorstellen'),
('record','L19;L22','Geregistreerde beschrijving die naar een referent kan verwijzen','entiteit; dataset','Meerdere records kunnen één referent beschrijven'),
('master record','L19;P01','Aangewezen beheerrecord in een bron- of hubcontext','golden record','Selectie- en bronstatus zijn organisatieafhankelijk'),
('golden record','L19;P01','Geïntegreerde keuze van gegevens volgens selectiebeleid','waarheid; gezaghebbende registratie','Golden duidt geen zelfstandige juridische of epistemische status aan'),
('reference data','L19','Waardenstelsels voor toegestane of gedeelde classificaties','masterdata-entiteiten','L19 gebruikt ook een ruimere proceduregerichte formulering'),
('metadata','S07;S08;S47','Informatie over betekenis, representatie, beheer of aanbod','uitsluitend technisch schema','Registries en catalogi hebben overlappende maar verschillende constructies'),
('dataset','S47;S09','Afgebakende gegevensverzameling in catalogus- of registratiecontext','dataproduct; individuele entiteit','11179-33 omvat ook datasetregistratie'),
('data product','L12;L20;S51','Beheerd aanbod gericht op terugkerende informatiebehoefte','dataset; masterdata','Productdenken bestond eerder dan recente Data Mesh-terminologie'),
('masterdata','B01;L20;L18','Herhaald gebruikte entiteitsgegevens met afgestemd beheer in een organisatiecontext','transactionele data; dataset','Eigen werkdefinitie; bronaccenten blijven verschillend'),
('transactionele data','L20;P01','Gegevens over gebeurtenissen of handelingen','transactional MDM','Het architectuurlabel betreft beheer van masterdatamutaties'),
('operationele/analytische data','L20','Gebruik in uitvoering respectievelijk analyse','masterdata als beheerd domein','Geen wederzijds uitsluitende classificatie met masterdata'),
('provenance/lineage','S33','Herkomstcontext respectievelijk gevolgde transformatieketen','waarheid; bevoegdheid','Eigen praktische werkafbakening; geen universele bronconsensus'),
('valid time/transaction time','L14','Geldigheid in werkelijkheid versus aanwezigheid als actuele databasekennis','ontvangsttijd afnemer','Te betrekken op expliciet genoemd bron- of afnemerssysteem')]
rows=[]
for i,(term,ids,definition,other,ambiguity) in enumerate(concept_data,1):
 rows.append(dict(concept_id=f'K{i:02}',term=term,source_id=ids,brondefinitie=definition,bronlocatie=';'.join('EX-'+x for x in ids.split(';')),betekeniscontext='Parafrase/analytische werkafbakening; geen letterlijk normcitaat',onderscheid_met=other,tegenstrijdigheden=ambiguity,analyse_status='Voorlopige bronvergelijking; onafhankelijk te beoordelen'))
write('concepts.csv',rows)
gaps=[('Capability-taxonomie','Vergelijkbaarheid bij verschillende granulariteit','L20;L05;P01','Uiteenlopende bestaande taxonomieën','synthesevraag'),('Expliciete semantiek','Voorwaarden voor additionele waarde van formalisering','L18;L13;L20','Semantische MDM en business semantics bestonden reeds','conditionele effectvraag'),('Federatie','Vergelijking onder gelijke taak- en kostendefinities','L20;L23;L24','Bestaande architectuurvergelijkingen beperken nieuwheidsclaim','vergelijkingsvraag'),('Gezag en identiteit','Interpretatie van identiteit, herkomst en institutioneel gezag','L21;S33;S25','Afzonderlijke bouwstenen bestaan','integratievraag'),('Historie','Behoud van tijdsbetekenis bij bron- en modelwijziging','L14;S08;S13','Bitemporele begrippen en metadatamodellen bestaan','contextgebonden vraag'),('AI-consumptie','Effect van contextmetadata bij masterdatataken','L16;L31','RAG/xLP-resultaten bestaan maar zijn taakgebonden','empirische vervolgvraag'),('Normtoegang','Volledige toepasselijke ISO/NEN-clausules ontbreken','S03;S08;S17','Catalogusbeperking is geen tekort van de norm','toegangslacune'),('Corpusdekking','FDS, semantic layers, data contracts en AI-agents beperkt gedekt','S27;S51;L16','Aangrenzende bronnen vervangen geen gerichte review','corpuslacune')]
write('gaps.csv',[dict(gap_id=f'RG{i:02}',thema=t,voorgesteld_hiaat=q,source_ids=s,zoekdekking='Gerichte bronselectie; geen uitputtende databasezoekactie',tegenbewijs=c,type_hiaat=k,status='voorlopig; geen aangetoond wereldwijd kennistekort') for i,(t,q,s,c,k) in enumerate(gaps,1)])
# Make method and access information useful without claiming unread articles were reviewed.
updates={
'L27':('Literatuurreview; abstract, selectie en conclusie gelezen','Verband MDM-frameworks en governancevolwassenheid onderzoeken','Verwant overzicht; geen eigen causale effectschatting'),
'B01':('Professionele inleiding; hoofdstukfragment','MDM-doelen en functies duiden','Definities en bedrijfssemantiek'),
'P01':('Leveranciershandboek; geselecteerde modelleerhoofdstukken','MDM-modellering en implementatiestijlen beschrijven','Patronen; historie; survivorship'),
'P02':('Leveranciershandboek; integratiebeschrijving','MDM en SaaS verbinden','Distributie; integratie'),
'L20':('Requirementsstudie; theoretisch kader en tabellen geanalyseerd','Strategische businessrequirements voor MDM-systemen','Capabilitiestaxonomie; vroeg productdenken'),
'L21':('Onderzoekstutorial','Entity-resolutiononderzoek structureren','Identiteit en matching'),
'L22':('Vergelijking van ER-evaluatiemaatstaven','ER-resultaten beoordelen','Metricafhankelijkheid'),
'L23':('Systematische grijze-literatuurreview van 114 bijdragen, volgens auteurs','Data Mesh-principes, capabilities en rollen structureren','Federatie; professioneel bewijs onderscheiden'),
'L24':('Literatuurreview met vergelijkingskader; 189 bijdragen volgens abstract','Datamanagementbenaderingen afbakenen','Architecturen en governance'),
'L29':('Survey; auteursversie 2020','End-to-end entity resolution structureren','ER-workflows'),
'L30':('Survey; auteursversie 2020','Blocking en filtering vergelijken','Kandidaatselectie en schaalbaarheid'),
'L31':('Methode-/demonstratiebeschrijving; depotversie 2024','Link prediction in MDM uitlegbaar maken','AI-hulpmiddel; beperkte overdraagbaarheid'),
'M01':('Ontwikkeling van rapportagechecklist en toelichting','Scoping-reviewrapportage verbeteren','Reviewtransparantie'),
'M02':('Ontwikkeling van rapportagerichtlijn en toelichting','Zoekrapportage verbeteren','Reproduceerbaarheid')}
for name in ['sources.csv','literature-matrix.csv']:
 rs=read(name)
 for r in rs:
  if r['id'] not in updates:continue
  method,purpose,relevance=updates[r['id']];r['methode']=method
  if name=='sources.csv':r.update(onderzoeksdoel=purpose,relevantie_mdm=relevance)
  else:r.update(onderzoeksvraag=purpose,relevantie_paper=relevance)
 with (E/name).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rs[0]));w.writeheader();w.writerows(rs)
print('22 conceptanalyses en 8 begrensde onderzoeksvragen geregistreerd.')
