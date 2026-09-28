"""Build navigable acquisition catalog, without converting downloads into findings."""
import csv,hashlib,html,json,re,shutil,subprocess
from pathlib import Path
from collections import Counter,defaultdict
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[2];BASE=ROOT/'research';E=BASE/'evidence'
def read(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(p,rows,fields):
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
class Text(HTMLParser):
 def __init__(self):super().__init__();self.depth=0;self.parts=[]
 def handle_starttag(self,t,a):
  if t in ('script','style','noscript'):self.depth+=1
  if t in ('p','div','br','li','section','h1','h2','h3','tr'):self.parts.append('\n')
 def handle_endtag(self,t):
  if t in ('script','style','noscript') and self.depth:self.depth-=1
 def handle_data(self,data):
  if not self.depth:self.parts.append(data)
legacyS=read(ROOT/'standards-matrix.csv');legacyL=read(ROOT/'literature-matrix.csv');new=read(E/'new-source-candidates.csv');downloads=read(E/'downloads.csv')
sources=[]
for r in legacyS:
 sources.append(dict(id=r['id'],titel=r['standaard'],auteur=r['organisatie_eigenaar'],jaar='',type=r['type_document'],publisher=r['organisatie_eigenaar'],doi_url=r['primaire_bron'],peer_reviewed='niet vastgesteld; officiële/professionele bron',primair_secundair='primaire bron voor eigen scope; interpretatie apart',onderzoeksdoel=r['toepassingsgebied'],methode='norm-/specificatie-/kaderanalyse nog uit te voeren',relevante_definities='nog niet opnieuw geëxtraheerd',belangrijkste_bevindingen='zie legacy-matrix; niet opnieuw inhoudelijk geverifieerd',beperkingen=r['bewijsniveau'],relevantie_mdm=r['relatie_master_data'],themas=r['abstractieniveau'],citatie=f"{r['organisatie_eigenaar']}. {r['standaard']}. {r['versie']}. {r['primaire_bron']}",selectiestatus='legacy_startcorpus; opnieuw te screenen',metadata_bron='standards-matrix.csv'))
for r in legacyL:
 sources.append(dict(id=r['id'],titel=r['titel'],auteur=r['auteur'],jaar=r['jaar'],type=r['publicatietype'],publisher='zie legacy-bron; niet apart geëxtraheerd',doi_url=r['doi_of_stabiele_bron'],peer_reviewed='ja volgens legacy-matrix; niet opnieuw geverifieerd' if 'Peer-reviewed' in r['publicatietype'] else 'zie publicatietype; niet opnieuw vastgesteld',primair_secundair='te classificeren per claimgebruik',onderzoeksdoel=r['onderzoeksvraag'],methode=r['methode'],relevante_definities='nog niet opnieuw geëxtraheerd',belangrijkste_bevindingen=r['belangrijkste_bevinding'],beperkingen=r['bewijsniveau']+'; '+r['beperkingen'],relevantie_mdm=r['relevantie_paper'],themas='legacy; thematische hercodering nodig',citatie=f"{r['auteur']} ({r['jaar']}). {r['titel']}. {r['doi_of_stabiele_bron']}",selectiestatus='legacy_startcorpus; opnieuw te screenen',metadata_bron='literature-matrix.csv'))
sources+=new
lookup={s['id']:s for s in sources};assert len(lookup)==len(sources)
artifacts=[];by_source=defaultdict(list);hashes=defaultdict(list)
for r in downloads:
 p=ROOT/r['local_path'] if r['local_path'] else None
 if r['retrieval_status']=='downloaded' and p and p.exists():
  if p.read_bytes().startswith(b'\xff\xd8\xff'):
   dest=BASE/'corpus'/'access-responses'/p.with_suffix('.jpg').name;dest.parent.mkdir(exist_ok=True);p.rename(dest);p=dest;r.update(local_path=str(p.relative_to(ROOT)),retrieval_status='non_document_asset',error='Linked thumbnail image; not a source document')
  elif p.stat().st_size==0 or str(r['http_status'])=='202':r.update(retrieval_status='incomplete_response',error='Empty body or HTTP 202; not acquired document')
  elif p.suffix=='.html':
   raw=p.read_text(errors='replace');title=re.search(r'<title[^>]*>(.*?)</title>',raw,re.I|re.S)
   title=html.unescape(re.sub(r'\s+',' ',title[1])).strip() if title else ''
   if re.search(r'^(Redirecting|Just a moment|Access Denied|Client Challenge|Robot Check)',title,re.I) or 'enable javascript' in raw.lower() and len(raw)<5000:
    r.update(retrieval_status='access_response',error='Redirect/challenge page; not source content')
   else:
    parser=Text();parser.feed(raw);text=re.sub(r'\n[ \t]*\n+', '\n\n',''.join(parser.parts))
    dest=BASE/'corpus'/'text'/p.with_suffix('.txt').name;dest.parent.mkdir(exist_ok=True);dest.write_text(text);r['text_path']=str(dest.relative_to(ROOT))
 if r['retrieval_status']!='downloaded':continue
 assert p and p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
 text=(ROOT/r['text_path']).read_text(errors='replace') if r['text_path'] else ''
 first=' '.join(text.split())[:320]
 parent_candidate=r['document_scope']=='linked_pdf_candidate_not_yet_screened'
 artifact=dict(artifact_id='D-'+r['source_id']+'-'+r['sha256'][:12],source_id=r['source_id'],parent_source_title=lookup[r['source_id']]['titel'],local_path=r['local_path'],text_path=r['text_path'],url=r['url'],sha256=r['sha256'],document_scope=r['document_scope'],first_text_excerpt=first,content_review='not_content_reviewed',identity_status='linked_document_not_identical_to_parent_by_default' if parent_candidate else 'identity_to_verify',screening_note='')
 if 'Dewey Decimal Classification' in first:artifact.update(identity_status='linked_background_document',screening_note='Buiten kern-MDM-selectie; niet als DCAT-AP-tekst behandelen.')
 if not text.strip():artifact['screening_note']='Geen doorzoekbare tekst; OCR/visuele inspectie nodig.'
 artifacts.append(artifact);by_source[r['source_id']].append(artifact);hashes[r['sha256']].append(r['local_path'])
for s in sources:
 files=by_source[s['id']];s['local_files']=';'.join(x['local_path'] for x in files);s['acquisition_status']='bestanden beschikbaar; aard en inhoud controleren' if files else 'geen bruikbare tekst verworven';s['download_count']=len(files)
write(E/'sources.csv',sources,list(sources[0]));write(E/'downloads.csv',downloads,list(downloads[0]));write(E/'artifacts.csv',artifacts,list(artifacts[0]))
# New-phase matrices retain original column names and distinguish inherited material.
stdfields=list(legacyS[0])+['corpus_status','inhoudelijke_extractie','jaar','relatie_metadata','relatie_data_quality','relatie_technical_interoperability','complementaire_standaarden']
std=[dict(r,corpus_status='legacy; opnieuw te screenen',inhoudelijke_extractie='Niet opnieuw uitgevoerd') for r in legacyS]
for r in new:
 if r['id'].startswith('S'):std.append(dict(id=r['id'],standaard=r['titel'],organisatie_eigenaar=r['auteur'],primaire_bron=r['metadata_bron'],corpus_status='kandidaat',inhoudelijke_extractie='Nog niet uitgevoerd',bewijsniveau='Officiële overzichtspagina; geen volledige norm'))
write(E/'standards-matrix.csv',std,stdfields)
litfields=list(legacyL[0])+['corpus_status','inhoudelijke_extractie']
lit=[dict(r,corpus_status='legacy; opnieuw te screenen',inhoudelijke_extractie='Niet opnieuw uitgevoerd') for r in legacyL]
for r in new:
 if not r['id'].startswith('S'):lit.append(dict(id=r['id'],auteur=r['auteur'],jaar=r['jaar'],titel=r['titel'],publicatietype=r['type'],onderzoeksvraag=r['onderzoeksdoel'],methode=r['methode'],belangrijkste_bevinding=r['belangrijkste_bevindingen'],relevantie_paper=r['relevantie_mdm'],beperkingen=r['beperkingen'],doi_of_stabiele_bron=r['doi_url'],bewijsniveau='Ontdekkingsmetadata; inhoudelijke extractie nog niet uitgevoerd',bronlocatie=r['metadata_bron'],geraadpleegd_op='2026-09-08',corpus_status='kandidaat',inhoudelijke_extractie='Nog niet uitgevoerd'))
write(E/'literature-matrix.csv',lit,litfields)
# Preserve old claims separately; do not republish design claims as review conclusions.
legacy=E/'legacy';legacy.mkdir(exist_ok=True)
for fn in ['claims-register.csv','standards-matrix.csv','literature-matrix.csv']:
 dest=legacy/fn
 if not dest.exists():shutil.copy2(ROOT/fn,dest)
for fn,fields in [('claims-register.csv',['claim_id','claim','classificatie','source_ids','bronpassages','bewijsstatus','tegenbronnen','rationale','beperkingen']),('concepts.csv',['concept_id','term','source_id','brondefinitie','bronlocatie','betekeniscontext','onderscheid_met','tegenstrijdigheden','analyse_status']),('gaps.csv',['gap_id','thema','voorgesteld_hiaat','source_ids','zoekdekking','tegenbewijs','type_hiaat','status'])]:
 if not (E/fn).exists():write(E/fn,[],fields)
write(E/'access-register.csv',[dict(source_id=r['source_id'],url=r['url'],status=r['retrieval_status'],http_status=r['http_status'],error=r['error'],follow_up='Legitieme alternatieve bron of reguliere toegang onderzoeken; geen inhoudelijke afwezigheidsclaim') for r in downloads if r['retrieval_status']!='downloaded'],['source_id','url','status','http_status','error','follow_up'])
write(E/'duplicates.csv',[dict(sha256=h,paths=';'.join(p),note='Identieke bytes; verschillende source-ID of URL kan hetzelfde werk aanduiden.') for h,p in hashes.items() if len(p)>1],['sha256','paths','note'])
summary=dict(source_records=len(sources),download_routes=len(downloads),usable_files=len(artifacts),pdf_files=sum(a['local_path'].endswith('.pdf') for a in artifacts),html_files=sum(a['local_path'].endswith('.html') for a in artifacts),unique_file_hashes=len(hashes),sources_with_files=len(by_source),failed_or_incomplete_routes=sum(r['retrieval_status']!='downloaded' for r in downloads),total_bytes=sum(int(r['bytes'] or 0) for r in downloads if r['retrieval_status']=='downloaded'),note='Acquisition counts, not independent studies or completed reviews.')
(E/'download-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
esc=html.escape
cards=[]
for s in sources:
 files=[]
 for a in by_source[s['id']]:
  relative='../'+a['local_path'];text='../'+a['text_path'] if a['text_path'] else ''
  label=Path(a['local_path']).suffix[1:].upper()
  files.append(f'<li><a href="{esc(relative)}">{label}</a> '+(f'<a href="{esc(text)}">Doorzoekbare tekst</a>' if text else '')+f' <small>{esc(a["document_scope"])}</small><details><summary>Bestandsidentiteit en herkomst</summary><p>{esc(a["first_text_excerpt"])}</p><p>{esc(a["screening_note"])}</p><a href="{esc(a["url"])}">Oorspronkelijke URL</a><p class="hash">SHA-256: {a["sha256"]}</p></details></li>')
 cards.append(f'<article data-search="{esc((s["id"]+" "+s["titel"]+" "+s["auteur"]+" "+s["themas"]+" "+s["type"]).lower(),quote=True)}"><span class="tag">{esc(s["id"])} · {esc(s["type"])}</span><h2>{esc(s["titel"])}</h2><p>{esc(s["auteur"])} · {esc(s["jaar"])}</p><p class="muted">{esc(s["acquisition_status"])}</p><ul>{"".join(files) or "<li>Geen bruikbaar document opgehaald; zie het toegangsregister.</li>"}</ul><details><summary>Bronmetadata en bewijsgrens</summary><p>{esc(s["beperkingen"])}</p><p>{esc(s["selectiestatus"])}</p><p>{esc(s["citatie"])}</p></details></article>')
page='''<!doctype html><html lang="nl"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MDM-onderzoek — lokale bronnenbibliotheek</title><style>body{font:16px/1.5 system-ui,sans-serif;background:#f2f5f7;color:#182f40;margin:0}header,main{max-width:1100px;margin:auto;padding:30px}header{padding-bottom:10px}h1{font-size:36px;line-height:1.15}h2{font-size:20px}input{width:100%;box-sizing:border-box;padding:14px;font:inherit;border:1px solid #7c959d;border-radius:8px}article{background:white;border:1px solid #d5e0e3;border-radius:9px;padding:22px;margin:18px 0}a{color:#076b70}small,.muted{color:#596976}li{margin:10px 0}.tag{font-size:13px;font-weight:600;color:#376773}details{font-size:14px;margin:10px 0}summary{cursor:pointer}.hash{overflow-wrap:anywhere;font-size:11px}.notice{padding:16px;border-left:4px solid #138c82;background:#e0f2ed}nav a{margin-right:20px}.count{font-size:14px}</style><header><h1>MDM-onderzoek<br>Lokale bronnenbibliotheek</h1><p>Boeken, papers, standaarden en professionele documentatie · verwerving 8 september 2026</p><p class="notice">Bestanden zijn verzameld, niet automatisch inhoudelijk beoordeeld. Een PDF kan een proefhoofdstuk, advies of bijlage zijn. Gelinkte documenten zijn niet automatisch de hoofdpublicatie. Het prototype valt buiten deze onderzoeksfase.</p>'''+f'<p>{summary["source_records"]} bronvermeldingen · {summary["usable_files"]} bestanden · {summary["pdf_files"]} PDF’s · {summary["unique_file_hashes"]} unieke bestandshashes</p>'+'''<nav><a href="evidence/sources.csv">Bronnenregister</a><a href="evidence/access-register.csv">Toegangsbeperkingen</a><a href="research-protocol.md">Protocol</a></nav><p><label for="q">Zoek op titel, auteur, thema of bron-ID</label></p><input id="q" type="search" placeholder="Bijvoorbeeld: matching, governance, ISO, B06"><p class="count" id="count" aria-live="polite"></p></header><main>'''+''.join(cards)+'''</main><script>const q=document.querySelector('#q'),a=[...document.querySelectorAll('article')];function filter(){const terms=q.value.toLowerCase().split(/\\s+/).filter(Boolean);let n=0;a.forEach(x=>{x.hidden=!terms.every(t=>x.dataset.search.includes(t));if(!x.hidden)n++});document.querySelector('#count').textContent=n+' bronvermeldingen zichtbaar'}q.addEventListener('input',filter);filter()</script></html>'''
(BASE/'index.html').write_text(page)
print(json.dumps(summary,indent=2))
