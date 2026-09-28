"""Generate the overview paper's bibliography and traceability from its own corpus.
Does not modify the older design-science manuscript or acquire sources.
"""
import csv, re, hashlib, json
from pathlib import Path
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[2]; E=ROOT/'research/evidence'; P=ROOT/'research/paper'
def read(name):
 with (E/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(name,rows,fields=None):
 if fields is None: fields=list(rows[0])
 with (E/name).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
def esc(x):
 return ''.join({'&':r'\&','%':r'\%','_':r'\_','#':r'\#','$':r'\$','{':r'\{','}':r'\}'}.get(c,c) for c in str(x))
def plain(x):
 x=re.sub(r'\\(?:paren|text)cite(?:\[[^\]]*\])?\{[^}]*\}','',x)
 x=re.sub(r'\\claim\{[^}]*\}','',x)
 x=re.sub(r'\\\w+\{([^{}]*)\}',r'\1',x)
 return ' '.join(x.replace('\\','').split())
class HTMLText(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.hide=0
 def handle_starttag(self,t,a):
  if t in ('script','style'):self.hide+=1
  if t in ('p','div','li','tr','h1','h2','h3'):self.parts.append('\n')
 def handle_endtag(self,t):
  if t in ('script','style'):self.hide=max(0,self.hide-1)
 def handle_data(self,d):
  if not self.hide:self.parts.append(d)
sources=read('sources.csv'); sf=list(sources[0]); src={r['id']:r for r in sources}
std=read('standards-matrix.csv'); lit=read('literature-matrix.csv'); arts=read('artifacts.csv')
for sid,title,url in [('F01',"Pas toe of leg uit-standaarden (verplicht)",'https://www.forumstandaardisatie.nl/open-standaarden/verplicht'),('F02','MIM: officiële standaardregistratie','https://www.forumstandaardisatie.nl/open-standaarden/mim'),('F03','Standaarden in behandeling','https://www.forumstandaardisatie.nl/standaarden-in-behandeling')]:
 if sid not in src:
  r=dict.fromkeys(sf,'');r.update(id=sid,titel=title,auteur='Forum Standaardisatie',jaar='2026',type='officiële lijstregistratie',publisher='Forum Standaardisatie',doi_url=url,peer_reviewed='nee; officiële registratie',primair_secundair='primair voor lijststatus',onderzoeksdoel='Formele Nederlandse lijststatus onderscheiden van technische versie',methode='Gerichte lijstcontrole',beperkingen='Momentopname 9 september 2026; toepasselijkheid vergt eigen beoordeling',metadata_bron=url);sources.append(r);src[sid]=r
fix={'L27':('Leonardo Guerreiro; José Martins; Maria do Rosário Bernardo; Henrique Mamede; Frederico Branco','2025'),'L22':('David Menestrina; Steven Euijong Whang; Hector Garcia-Molina','2010'), 'L24':('Anna Gieß; Andreas Hutterer','2025'),'L29':('Vassilis Christophides; Vasilis Efthymiou; Themis Palpanas; George Papadakis; Kostas Stefanidis','2020'),'L30':('George Papadakis; Dimitrios Skoutas; Emmanouil Thanos; Themis Palpanas','2020'),'L23':('Abel Goedegebuure; Indika Kumara; Stefan Driessen; Willem-Jan van den Heuvel; Geert Monsieur; Damian Andrew Tamburri; Dario Di Nucci','2023'), 'L31':('Balaji Ganesan; Sumit Bhatia; Hima Patel; Sameep Mehta; Matheen Ahmed Pasha; Srinivasa Parkala; Neeraj R Singh; Gayatri Mishra; Somashekhar Naganna','2024'),'M01':('Andrea C. Tricco; Erin Lillie; Wasifa Zarin; others','2018'),'M02':('Melissa L. Rethlefsen; Shona Kirtley; Siw Waffenschmidt; Ana Patricia Ayala; David Moher; Matthew J. Page; Jonathan B. Koffel; {PRISMA-S Group}','2021')}
for sid,(author,year) in fix.items(): src[sid].update(auteur=author,jaar=year)
src['M02'].update(publisher='Journal of the Medical Library Association',doi_url='https://doi.org/10.5195/jmla.2021.962')
src['S43']['doi_url']='https://ec.europa.eu/isa2/sites/default/files/eif_brochure_final.pdf'
# Archive supplementary primary documents separately from the acquisition snapshot.
for sid in ['F01','F02','F03','S42','S43']:
 paths=list((ROOT/'research/corpus/standards').glob(sid+'-paper-check-20260909.*'))
 for path in paths:
  tp=ROOT/'research/corpus/text'/path.with_suffix('.txt').name
  if path.suffix=='.html':
   parser=HTMLText();parser.feed(path.read_text(errors='replace'));tp.write_text(''.join(parser.parts),encoding='utf-8')
  if not any(a['local_path']==str(path.relative_to(ROOT)) for a in arts):
   arts.append(dict(artifact_id='D-'+sid+'-papercheck',source_id=sid,parent_source_title=src[sid]['titel'],local_path=str(path.relative_to(ROOT)),text_path=str(tp.relative_to(ROOT)),url=src[sid]['doi_url'],sha256=hashlib.sha256(path.read_bytes()).hexdigest(),document_scope='primary_document_supplement',first_text_excerpt='Supplement paperfase',content_review='selected_passages',identity_status='title_and_scope_checked',screening_note='Aanvulling; buiten verwervingssnapshot van 8 september'))
  src[sid]['local_files']=';'.join(sorted(set(filter(None,src[sid]['local_files'].split(';')+[str(path.relative_to(ROOT))]))))
# Known representation selection: PDF authors' versions and genuine article abstracts.
preferred={'B07':'B07-36c77dd26b','B01':'B01-6f746e01b6','P01':'P01-28c1969531','P02':'P02-1d27e6dcf1','L05':'L05-db1aa40d98','L07':'L07-3a4864a17e','L08':'L08-994a4f9d9d','L10':'L10-af5b66b3f5','L11':'L11-04815b51c3','L12':'L12-296d8d70e7','L13':'L13-5abd6a1f6a','L14':'L14-fa94e82c7b','L15':'L15-ecf4996ea9','L16':'L16-649aaeda18','L18':'L18-2be5982312','L19':'L19-a9de6de4c9','L20':'L20-ef53704b6c','L21':'L21-a43adcb079','L22':'L22-265ff3c24d','L23':'L23-e486d09f75','L27':'L27-ba0383324b','L24':'L24-fc9d53d5bb','L29':'L29-1ff494de9c','L30':'L30-024a111af7','L31':'L31-decc8c232d','M01':'M01-501e205a9e','M02':'M02-5062d21895','S42':'S42-paper-check','S43':'S43-paper-check'}
# Extraction anchors and paraphrases; these are not invented verbatim quotations.
notes={
'L27':('CONCLUSION','Abstract; selectiemethode; conclusie en limitations','Review verbindt MDM en governancevolwassenheid, maar plaatst empirische kadervalidatie in vervolgonderzoek.'),
'B07':('schema','Boekhoofdstukken over schema en context','Boekversie van knowledge graph-overzicht; geen onafhankelijk bewijs naast L13.'),
'B01':('1.1','§1.1–1.3, §1.5 en §1.9 (hoofdstukfragment)','MDM behandelt uiteenlopende representaties en bedrijfsbetekenis; beheermiddelen dienen bedrijfsdoelen.'),
'P01':('Registry','Gedrukte pp. 42–46, 226–227 en 417','Patroonlabels onderscheiden verwijzingen, primair beheer en synchronisatie; historie en survivorship zijn afzonderlijke functies.'),
'P02':('integration','Scope, inhoudsopgave en integratiebespreking','Leveranciersbeschrijving van MDM-integratie met SaaS; geen onafhankelijke effectvergelijking.'),
'L05':('Abstract','Uitgeversabstract','Functioneel referentiemodel voor masterdatakwaliteitsmanagement; inhoudelijke detaillering beperkt door abstracttoegang.'),
'L07':('governance','Auteursinstellingsabstract','Review ordent data governance als gezag en controle over gegevensbeheer.'),
'L08':('identity','Theoretische hoofdstukken over identiteit en ontologische categorieën','Ontologische analyse maakt aannames van conceptuele modellen expliciet.'),
'L10':('rigidity','Taxonomische meta-eigenschappen','OntoClean analyseert taxonomieën met onder meer identiteit en rigiditeit.'),
'L11':('machine','FAIR-principes en machine-actionability','Vindbaarheid, toegankelijkheid, interoperabiliteit en hergebruik zijn onderscheiden principes.'),
'L12':('product','Definities en vergelijking, tabel 1','Data products, mesh en fabric worden als gerelateerde maar verschillende benaderingen besproken.'),
'L13':('schema','Overzicht, schema, identiteit en context','Knowledge graphs omvatten meerdere representatie- en redeneermogelijkheden.'),
'L14':('valid time','Glossary: valid time en transaction time','Geldigheid in de werkelijkheid verschilt van aanwezigheid als databasekennis.'),
'L15':('consumer','Uitgeversabstract','Datakwaliteit wordt vanuit het perspectief van gegevensconsumenten onderzocht.'),
'L16':('retrieval','Abstract en methode','Retrieval-augmented generation verbindt generatie met opgehaalde informatie; resultaten zijn taakgebonden.'),
'L18':('virtual','SMDM-architectuur en demonstratie','Virtuele RDF-toegang, ontologieën en mappings zijn bestaande semantische MDM-bouwstenen.'),
'L19':('quality','§2, tabellen 1–3 en model-/meetbeschrijving','Kwaliteitsmodel voor masterdatarepositories koppelt dimensies en metingen aan internationale standaarden.'),
'L20':('Business Semantics','Theoretisch kader p. 2–3; tabellen 1–2 p. 6–7','Master Data as a Product en Business Semantics Management zijn expliciete vroegere MDM-ideeën.'),
'L21':('entity resolution','Abstract en tutorialdoel','Entity resolution koppelt verschillende beschrijvingen van dezelfde referent.'),
'L22':('measures','Abstract en vergelijking van maatstaven','Evaluatiematen kunnen dezelfde ER-uitkomsten verschillend rangschikken.'),
'L23':('114','Abstract en vier principes; auteursversie 2023','Review van grijze literatuur synthetiseert Data Mesh-principes; praktijkclaims zijn geen onafhankelijk gemeten effecten.'),
'L24':('189','Abstract en vergelijkingskader','Review vergelijkt platforms, spaces, meshes en fabrics; classificatie bepaalt geen lokale prestatiegarantie.'),
'L29':('workflows','Abstract en end-to-end overzicht; arXiv v3, 2020','Entity resolution kent meerdere samenhangende verwerkingsstappen.'),
'L30':('Blocking','Abstract; arXiv v4, 2020','Blocking en filtering beperken vergelijkingen op verschillende manieren.'),
'L31':('explain','Abstract en demonstratie; depotversie 2024','xLP illustreert uitlegbaarheid van voorspelde relaties in MDM.'),
'M01':('checklist','Checklist en toelichting','PRISMA-ScR ondersteunt transparante rapportage van scoping reviews.'),
'M02':('16','Abstract en rapportage-items','PRISMA-S ondersteunt reproduceerbare rapportage van literatuurzoekacties.'),
'S13':('conceptueel','§1.6 en beschouwingsniveaus','MIM onderscheidt modelniveaus en modelconstructies.'),
'S14':('5.4','§5.4 relatie informatiemodellen; §5.5 beheer','NL-SBB specificeert begripsbeschrijving en koppelingen met modellen en beheer.'),
'S31':('3.5.1','Concepten, labels en §3.5.1','SKOS maakt label en concept onderscheidbaar; concept en OWL-klasse zijn niet algemeen disjunct.'),
'S33':('Entity','PROV-O overview en kernconstructies','Entiteiten, activiteiten, agents en afleidingsrelaties representeren provenance.'),
'S34':('measurement','Quality measurement en herkomstvoorbeelden','DQV beschrijft kwaliteitsmetadata en metingen, niet zelfstandig feitelijke juistheid.'),
'S42':('Subject matter and scope','Artikel 1–2','De verordening adresseert grensoverschrijdende interoperabiliteit van trans-Europese digitale publieke diensten.'),
'S43':('four layers','§3, in het bijzonder §3.5','EIF onderscheidt juridische, organisatorische, semantische en technische interoperabiliteit.'),
'F01':('NL-SBB','Lijsttabel; gecontroleerd 9 september 2026','NL-SBB 1.0, OpenAPI 3.0, REST-regels 2.2 en CloudEvents 1.1 staan op de pas-toe-of-leg-uit-lijst.'),
'F02':('Aanbevolen','Status en versie','MIM 1.2 staat als aanbevolen geregistreerd.'),
'F03':('DCAT','Lijsttabel en versiewijzigingen','DCAT-AP-NL, MDTO en TOOI staan in behandeling; OpenAPI-versiewijziging naar 3.1 is in procedure.')}
# Resolve main-text citations before generating appendices.
bodyfiles=sorted((P/'sections').glob('0*.tex')); body='\n'.join(p.read_text() for p in bodyfiles)
used=set(k.strip() for group in re.findall(r'\\(?:paren|text)cite(?:\[[^\]]*\])?\{([^}]+)\}',body) for k in group.split(','))
assert not used-src.keys(),used-src.keys()
for sid,r in src.items():
 if sid not in used:r['selectiestatus']='niet aangehaald; kandidaat behouden'
# Linked material is not the book itself.
for a in arts:
 if 'B07-36c77dd26b' in a['local_path']:
  a.update(content_review='identiteitscontrole; geen boekbewijs',identity_status='linked_background_document',screening_note='Describing Linked Datasets; niet Knowledge Graphs. Niet aangehaald als B07.')
if 'B07' not in used:
 src['B07'].update(relevante_definities='Niet inhoudelijk gebruikt',belangrijkste_bevindingen='Geen boekbevinding afgeleid; gelinkte PDF is ander werk',acquisition_status='Catalogus en gelinkte documenten; boekidentiteit niet aangetoond')
extracts=[]; locs={}
for sid in sorted(used):
 candidates=[a for a in arts if a['source_id']==sid and a['text_path'] and (ROOT/a['text_path']).exists()]
 if sid in preferred:candidates.sort(key=lambda a:preferred[sid] not in a['text_path'])
 else:candidates.sort(key=lambda a:'linked_pdf_candidate' in a['document_scope'])
 keyword,anchor,paraphrase=notes.get(sid,('Abstract','Scope/introductie; zie bron en standaardenmatrix',src[sid]['onderzoeksdoel']))
 if candidates:
  a=candidates[0];tp=ROOT/a['text_path'];txt=tp.read_text(errors='replace');lines=txt.splitlines();i=next((i for i,x in enumerate(lines) if keyword.lower() in x.lower()),0)
  location=f"{a['text_path']}:regel {i+1}; {anchor}"; sourcefile=a['local_path'];sha=a['sha256'];tsha=hashlib.sha256(tp.read_bytes()).hexdigest()
  status='geselecteerde passage; geen integrale bronvalidatie'
  if sid in ['L05','L07','L15']:status='abstract; geen volledige artikelanalyse'
  if sid in ['S01','S17','S27']:status='officiële overzichts-/cataloguspagina; beperkte inhoudelijke dekking'
  a['content_review']=status;a['screening_note']=anchor
 else:
  sourcefile='research/evidence/iso-official-catalog-check.json' if sid in ['S02','S03','S07','S08','S09','S10','S11','S12'] else 'research/evidence/official-catalog-notes.md'
  q=ROOT/sourcefile;sha=hashlib.sha256(q.read_bytes()).hexdigest() if q.exists() else '';tsha=sha
  location=src[sid]['doi_url']+'; officieel abstract/overzicht; geen volledige norm';status='officiële webcontrole; alleen scope'
  paraphrase=next((s['toepassingsgebied'] for s in std if s['id']==sid),src[sid]['titel'])
 ex=dict(extract_id='EX-'+sid,source_id=sid,bronlocatie=location,local_file=sourcefile,sha256=sha,text_sha256=tsha,parafrase=paraphrase,bewijsstatus=status,beperking='Gerichte passagecontrole; toepassingsscope begrenst conclusies; geen effectbewijs uit normatieve bron.',geraadpleegd_op='2026-09-09')
 extracts.append(ex);locs[sid]=ex
 src[sid].update(selectiestatus='aangehaald in overzichtspaper; geselecteerde passages',relevante_definities=paraphrase,belangrijkste_bevindingen=paraphrase,primair_secundair='primair voor eigen inhoud; reviewliteratuur synthetiseert andere werken',methode=src[sid]['methode'] if 'nog niet' not in src[sid]['methode'] else 'Gerichte passageanalyse; onderzoeksmethode alleen binnen gelezen tekst',acquisition_status=status)
# Short analytic propositions; the manuscript contains their qualified full formulations.
summaries='''MDM omvat technische en organisatorische beheertaken.
Dataproducten en federatieve benaderingen overlappen met MDM zonder ermee samen te vallen.
Reviewrapportagerichtlijnen ondersteunen transparantie, geen automatisch systematische dekking.
Masterdatadefinities benadrukken domeinentiteiten, hergebruik en afgestemd beheer.
Een golden record is geen garantie van juistheid of institutioneel gezag.
Vroege MDM-publicaties bevatten semantisch en productgericht denken.
Vier theoretische perspectieven bieden een eigen ordening van het corpus.
Datacategorieën verschillen in classificatiegrond en zijn niet allemaal exclusief.
Capability-taxonomieën verschillen in granulariteit en doel.
De lifecycle is een cyclisch analysekader, geen universeel stappenvoorschrift.
Patroonlabels verschillen tussen MDM-bronnen.
Patroonlabels bepalen niet zelfstandig prestaties of consistentiegaranties.
Entity resolution omvat meer dan tekstvergelijking.
Identifiergelijkheid, recordgelijkheid en referentidentiteit verschillen.
Matching, survivorship en domeinverandering vragen verschillende besluiten.
ER-maatstaven kunnen verschillende rangordes opleveren.
Datakwaliteit is contextgebonden en multidimensionaal.
Kwaliteitsdimensies vereisen expliciete vergelijkingsconventies.
Normscope, kwaliteitsmetadata en graafvalidatie hebben verschillende toetsobjecten.
Governance adresseert besluitrechten en verantwoordelijkheid.
Roltermen vragen bron- en contextgebonden interpretatie.
Standaardbeheer is geen volledige data governance.
Metadataregistratie onderscheidt conceptuele en representatieconstructies.
Een technisch schema bepaalt niet zelfstandig de volledige betekenis.
Metadataregistries en catalogi hebben verschillende en overlappende scopes.
Term, definitie en begrip zijn te onderscheiden; begrip/concept zijn bronafhankelijk.
SKOS, NL-SBB en MIM hebben complementaire en overlappende functies.
Bedrijfssemantiek komt aantoonbaar voor in vroegere MDM-literatuur.
Gelijke labels garanderen geen gelijke begripsafbakening.
EIF-niveaus verschillen van de eigen uitsplitsing van syntaxis en structuur.
Conceptuele modellen veronderstellen ontologische categorieën en identiteit.
Ontologische modelleerbenaderingen zijn geen universele MDM-vereiste.
SKOS-concept, ontologische klasse, objecttype en data-element zijn geen automatische equivalenten.
Semantic Web-specificaties vervullen verschillende representatie- en queryfuncties.
SMDM is een bestaand antecedent van semantische MDM-integratie.
Een formeel valide graaf garandeert geen juiste mapping of broninhoud.
PROV-O biedt constructies voor provenance; lineage is hier een werkafbakening.
Herkomst is geen zelfstandige waarheids- of bevoegdheidswaarborg.
Valid time en transaction time zijn verschillende tijdsbetekenissen.
Tijdnotatie en tijdontologie bepalen geen volledig historiebeleid.
Documentsoort, normatieve status en empirisch bewijs zijn verschillende assen.
Cross-standard relaties vormen een synthese, geen verplichte componentenlijst.
Profielrelaties, complementaire metadata en onderzoekersmappings verschillen.
Overlap bewijst geen redundantie; scopebeperking bewijst geen wetenschappelijke lacune.
Basisregistratieafspraken verbinden kerngegevens met institutionele verantwoordelijkheid.
BAG biedt begripsdocumentatie; geen operationele stelselketen is hier onderzocht.
Nederlandse standaarden opereren op verschillende abstractieniveaus.
Nederlandse lijststatus en technische versie moeten afzonderlijk worden vastgesteld.
De FDS-dekking is te beperkt voor reconstructie van operationele afspraken.
EIF, Europese wetgeving en SEMIC hebben verschillende functies.
FAIR ondersteunt hergebruik en machinegericht gebruik zonder algemene openbaarheidseis.
Masterdata en dataproducten beschrijven verschillende aspecten van gegevensaanbod.
Masterdata als product is een expliciet eerder gepubliceerd idee.
Productmetadata overlappen met catalogus- en registratiemetadata.
Data Mesh-principes zijn beschreven in een grijze-literatuurreview.
Federatie heeft technische en organisatorische dimensies.
API- en eventstandaarden bepalen niet vanzelf domeinbetekenis.
Data contracts en API-first zijn hier begrensde onderzoeksoriëntaties.
AI kan hulpmiddel en consument van masterdata zijn; xLP is een beperkt voorbeeld.
RAG-resultaten bewijzen geen algemeen voordeel van semantische MDM.
Machineleesbare epistemische status is een open effect- en representatievraag.
Gegevens, representaties, beheer en consumptie vormen een eigen synthesemodel.
Gegevensrollen, correctheidsvormen en centralisatie-assen moeten worden onderscheiden.
Convergentie in geselecteerde bronnen is geen vastgestelde vakgebiedbrede consensus.
Uniformiteit, autonomie, modelleerlast en bruikbaarheid vormen analytische spanningen.
De onderzoeksagenda onderscheidt synthesevragen van corpus- en toegangslacunes.
Herbenoeming en technische vernieuwing blijven alternatieve interpretaties.
Integratieproblemen kunnen door ontbrekende toepassing in plaats van ontbrekende standaarden ontstaan.'''.splitlines()
assert len(summaries)==68
own={7,8,9,10,12,14,15,18,21,24,25,29,32,36,38,40,41,42,44,49,52,54,56,58,61,62,63,64,65,66,67,68}
claims=[];trace=[];appendix=[]
for file in bodyfiles:
 text=file.read_text()
 for m in re.finditer(r'\\claim\{(RC\d+)\}',text):
  cid=m[1];n=int(cid[2:]);start=text.rfind('\n\n',0,m.start());para=text[start+2:m.start()]; ids=set(k.strip() for g in re.findall(r'\\(?:paren|text)cite(?:\[[^\]]*\])?\{([^}]+)\}',para) for k in g.split(','))
  if n==42:ids={s for s in used if s.startswith('S')}
  if n==66:ids={'L20','L05','P01','L18','L13','L23','L24','L21','S33','S25','L14','S08','S13','L16','L31'}
  assert ids,(cid,para)
  ids=sorted(ids); sec=re.findall(r'\\section\{([^}]+)\}',text[:m.start()])[-1];ov='OV1' if n in range(4,9) else 'OV2' if n in range(9,13) else 'OV3' if n in range(13,23) or n in range(37,41) else 'OV4' if n in range(23,45) else 'OV5' if n in range(45,62) else 'OV6'
  cls='eigen synthese' if n in own else 'normatief' if all(s.startswith(('S','F')) for s in ids) else 'meerdere bronnen' if len(ids)>1 else 'één bron'
  claims.append(dict(claim_id=cid,claim=summaries[n-1],classificatie=cls,source_ids=';'.join(ids),bronpassages=';'.join('EX-'+s for s in ids),bewijsstatus='Broninterpretatie; geen eigen empirische toets',tegenbronnen='L20;L18' if n in (6,28,53,67) else '',rationale=plain(para),beperkingen='Zie per-bron toegangslimiet in source-extracts.csv. Eigen synthese is niet extern gevalideerd.'))
  trace.append(dict(research_question=ov,claim_id=cid,source_ids=';'.join(ids),extract_ids=';'.join('EX-'+s for s in ids),paper_section=sec,tex_file=str(file.relative_to(ROOT)),tex_line=text[:m.start()].count('\n')+1,claim_type=cls))
  appendix.append((n,f"{cid} & {esc(summaries[n-1])} & {esc(', '.join(ids))} \\\\\n"))
write('claims-register.csv',sorted(claims,key=lambda r:r['claim_id']));write('source-extracts.csv',extracts);write('paper-traceability.csv',trace)
head=r'\small\begin{longtable}{@{}P{.09\linewidth}P{.59\linewidth}P{.24\linewidth}@{}}'+'\n'+r'\toprule Claim & Analytische uitspraak & Bron-ID\textquotesingle s \\\midrule\endfirsthead'+'\n'+r'\toprule Claim & Analytische uitspraak & Bron-ID\textquotesingle s \\\midrule\endhead'+'\n'
(P/'sections/claims-table.tex').write_text(head+''.join(x[1] for x in sorted(appendix))+r'\bottomrule\end{longtable}\normalsize'+'\n')
# Bibliography keeps all corpus entries; only citations are printed.
old=(ROOT/'references.bib').read_text();entries={m[1]:m[0] for m in re.finditer(r'@\w+\{([^,]+),.*?\n\}',old,re.S)}
for sid,r in src.items():
 if sid in entries:
  if sid=='S43':entries[sid]=re.sub(r'url = \{[^}]*\}',r'url = {'+r['doi_url']+'}',entries[sid])
  if sid in locs:
   entries[sid]=re.sub(r'note = \{.*\}(?=,?\n)',lambda m:'note = {'+esc('Bron-ID '+sid+'. '+locs[sid]['bewijsstatus'])+'}',entries[sid])
  continue
 author=r['auteur'].replace('; ',' and ')
 if sid.startswith(('S','F')):author='{'+author+'}'
 year=re.search(r'\b(19|20)\d{2}\b',r['jaar']);year=year[0] if year else None
 fields={'author':author,'title':'{'+esc(r['titel'])+'}','url':r['doi_url'],'note':esc('Bron-ID '+sid+'. '+(locs[sid]['bewijsstatus'] if sid in locs else 'Kandidaat; niet inhoudelijk gebruikt.'))}
 if year:fields['year']=year
 if sid in ('L29','L30'):fields['note']+=esc(' Auteursversie 2020; eerste depot 2019; geen voorlopige DOI overgenomen.')
 if sid=='L31':fields['note']+=esc(' Depot 2024; document noemt tevens 2020 en 2022.')
 if sid=='B01':fields['note']+=esc(' Alleen hoofdstuk 1 geraadpleegd.')
 if sid=='L23':fields['note']+=esc(' Auteursversie 2023; grijze-literatuurreview.')
 if sid in ('P01','P02'):fields['note']+=esc(' Leveranciersliteratuur.')
 if sid=='M02':fields['doi']='10.5195/jmla.2021.962'
 if sid=='L24':fields['doi']='10.1007/s10257-025-00707-4'
 fields['urldate']='2026-09-09'
 entries[sid]='@misc{'+sid+',\n'+',\n'.join('  '+k+' = {'+v+'}' for k,v in fields.items())+'\n}'
def bib_ascii(t):
 import unicodedata
 accents={'\u0301':"'",'\u0300':'`','\u0308':'"','\u0302':'^','\u0303':'~','\u030c':'v','\u0327':'c'}
 out=[]
 for ch in t:
  d=unicodedata.normalize('NFD',ch)
  if len(d)==2 and d[1] in accents:out.append('{'+chr(92)+accents[d[1]]+'{'+d[0]+'}}')
  elif ch=='ß':out.append(r'{\ss}')
  else:out.append(ch)
 return ''.join(out)
(P/'references.bib').write_text(bib_ascii('% Overzichtspaper: alleen corpusbronnen; toegangsgrenzen per bron.\n\n'+'\n\n'.join(entries.values())+'\n'))
for s in std:
 sid=s['id']
 if sid in locs:
  s.update(corpus_status='geselecteerde passage gebruikt in overzichtspaper',inhoudelijke_extractie='EX-'+sid,bewijsniveau=locs[sid]['bewijsstatus'],bronlocatie=locs[sid]['bronlocatie'],geraadpleegd_op='2026-09-09')
 if sid=='S07':s['versie']='2023; Amd 1:2026 vermeld, inhoud niet geanalyseerd'
 if sid=='S52':s.update(versie='Serieoverzicht; 2019-delen vermeld',type_document='Officiële normoverzichtspagina',abstractieniveau='Datum- en tijdrepresentatie',toepassingsgebied='Notatie van datum en tijd',bewijsniveau='Officieel web-overzicht; geen volledige norm')
for r in lit:
 sid=r['id']
 if sid in locs:
  r.update(auteur=src[sid]['auteur'],jaar=src[sid]['jaar'],belangrijkste_bevinding=locs[sid]['parafrase'],bewijsniveau=locs[sid]['bewijsstatus'],bronlocatie=locs[sid]['bronlocatie'],geraadpleegd_op='2026-09-09',corpus_status='aangehaald; gerichte passageanalyse',inhoudelijke_extractie='EX-'+sid,doi_of_stabiele_bron=src[sid]['doi_url'])
write('sources.csv',sources,sf);write('standards-matrix.csv',std);write('literature-matrix.csv',lit);write('artifacts.csv',arts)
write('paper-selection.csv',[dict(source_id=s['id'],selection='aangehaald' if s['id'] in used else 'niet aangehaald; kandidaat behouden',reason='Relevante passage voor paperclaim' if s['id'] in used else 'Niet nodig voor afgebakende synthese of inhoudelijke dekking onvoldoende',evidence=locs[s['id']]['bewijsstatus'] if s['id'] in locs else 'Geen afgeronde inhoudelijke selectiebeoordeling') for s in sources])
rows=[]
for s in std:
 if s['id'] not in used:continue
 rows.append(esc(s['id']+' '+s['standaard'])+' & '+esc(s['versie']).replace('Onderzoeksreferenties:', 'Referenties:').replace('Organisation','Org.').replace('familieversie','familie\\-versie')+' & '+esc(s['abstractieniveau']+'. '+s['bewijsniveau'])+r' \\'+'\n')
(P/'sections/standards-table.tex').write_text('Dit overzicht noemt de gebruikte documentversies; het is geen verklaring van actuele conformiteit of verplichte gezamenlijke toepassing.\n'+r'\small\begin{longtable}{@{}P{.29\linewidth}P{.22\linewidth}P{.41\linewidth}@{}}'+'\n'+r'\toprule Document & Gebruikte versie & Niveau en bewijsgrens \\\midrule\endfirsthead'+'\n'+r'\toprule Document & Gebruikte versie & Niveau en bewijsgrens \\\midrule\endhead'+'\n'+''.join(rows)+r'\bottomrule\end{longtable}\normalsize'+'\n')
print(json.dumps({'claims':len(claims),'cited_sources':len(used),'source_records':len(sources),'extracts':len(extracts)},indent=2))
