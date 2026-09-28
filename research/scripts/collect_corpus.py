"""Retrieve public corpus documents; transport success is not scholarly verification.
Only explicitly registered URLs and at most three PDF links per source page.
No authentication, paywall bypass, recursive crawling, or external executable content.
"""
import csv,datetime,hashlib,json,re,urllib.request,urllib.parse,concurrent.futures,subprocess
from pathlib import Path
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[2]; BASE=ROOT/'research'; EV=BASE/'evidence'
MAX_BYTES=60*1024*1024
class Links(HTMLParser):
 def __init__(self):super().__init__();self.pdfs=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='meta' and a.get('name','').lower() in ('citation_pdf_url','eprints.document_url'):self.pdfs.append(a.get('content',''))
  if tag=='a' and re.search(r'\.pdf(?:$|[?#])',a.get('href',''),re.I):self.pdfs.append(a['href'])
def readcsv(p):
 if not p.exists():return []
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def writecsv(p,rows,fields):
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
def urls(value):return re.findall(r'https?://[^\s|;]+',value)
items=[]
for filename in ['standards-matrix.csv','literature-matrix.csv']:
 for r in readcsv(ROOT/filename):
  cat='standards' if r['id'].startswith('S') else 'papers'
  for field in (['primaire_bron','bron_lijststatus'] if cat=='standards' else ['doi_of_stabiele_bron','bronlocatie']):
   for u in urls(r.get(field,'')):items.append(dict(source_id=r['id'],url=u,category=cat,document_scope='source_document_or_landing_page',discovered_from='repository:'+filename+':'+field))
for r in readcsv(EV/'download-seeds.csv'):items.append(r)
seen=set();items=[r for r in items if not ((r['source_id'],r['url']) in seen or seen.add((r['source_id'],r['url'])))]
fields=['source_id','url','category','document_scope','discovered_from','retrieved_at','http_status','resolved_url','media_type','local_path','text_path','bytes','sha256','retrieval_status','review_status','error']
prior=readcsv(EV/'downloads.csv'); cache={(r['source_id'],r['url']):r for r in prior}
def fetch(item):
 old=cache.get((item['source_id'],item['url']))
 if old and old['retrieval_status']=='downloaded' and (ROOT/old['local_path']).exists():return old
 rec={k:item.get(k,'') for k in fields};rec.update(retrieved_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),review_status='not_content_reviewed',retrieval_status='failed')
 try:
  req=urllib.request.Request(item['url'],headers={'User-Agent':'Mozilla/5.0 (MDM academic corpus; public documents only)','Accept':'application/pdf,text/html,application/xhtml+xml,*/*;q=0.8'})
  with urllib.request.urlopen(req,timeout=25) as response:
   rec.update(http_status=response.status,resolved_url=response.url,media_type=response.headers.get('Content-Type',''))
   data=response.read(MAX_BYTES+1)
  if len(data)>MAX_BYTES:raise ValueError('Exceeds 60 MiB limit; not saved')
  if data.startswith(b'\xff\xd8\xff') or data.startswith(b'\x89PNG'):raise ValueError('Linked image is not a source document')
  if not data:raise ValueError('Empty response is not a source document')
  ext='pdf' if data.startswith(b'%PDF-') else ('html' if b'<html' in data[:8000].lower() or 'html' in rec['media_type'] else 'txt')
  # Challenge responses are retained separately, never counted as source documents.
  challenge=ext=='html' and bool(re.search(rb'<title[^>]*>\s*(?:Just a moment|Access Denied|Robot Check|Attention Required|Client Challenge)',data[:15000],re.I))
  folder=BASE/'corpus'/('access-responses' if challenge else item['category']);folder.mkdir(parents=True,exist_ok=True)
  path=folder/(item['source_id']+'-'+hashlib.sha256(item['url'].encode()).hexdigest()[:10]+'.'+ext)
  path.write_bytes(data)
  rec.update(local_path=str(path.relative_to(ROOT)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),retrieval_status='access_challenge' if challenge else 'downloaded')
  if ext=='pdf':
   info=subprocess.run(['pdfinfo',str(path)],capture_output=True,text=True)
   if info.returncode:rec.update(retrieval_status='invalid_pdf',error=info.stderr[:400])
   else:
    txt=BASE/'corpus'/'text'/path.with_suffix('.txt').name;txt.parent.mkdir(exist_ok=True)
    result=subprocess.run(['pdftotext','-layout',str(path),str(txt)],capture_output=True,text=True)
    if not result.returncode:rec['text_path']=str(txt.relative_to(ROOT))
 except Exception as e:rec['error']=str(e)[:500]
 return rec
results=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
 for r in pool.map(fetch,items):
  results.append(r)
  print(r['source_id'],r['retrieval_status'],r.get('bytes',''),flush=True)
writecsv(EV/'downloads.csv',results,fields)
# One-hop links are retrieval candidates. Relevance and full-text identity still need review.
children=[]
for r in results:
 if r['retrieval_status']!='downloaded' or not r['local_path'].endswith('.html'):continue
 try:
  parser=Links();parser.feed((ROOT/r['local_path']).read_text(errors='replace'))
  for link in list(dict.fromkeys(parser.pdfs))[:3]:
   u=urllib.parse.urljoin(r['resolved_url'],link)
   if not u.startswith(('https://','http://')) or (r['source_id'],u) in seen:continue
   seen.add((r['source_id'],u));children.append(dict(source_id=r['source_id'],url=u,category=r['category'],document_scope='linked_pdf_candidate_not_yet_screened',discovered_from=r['url']))
 except Exception:pass
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 for r in pool.map(fetch,children):results.append(r);print('linked',r['source_id'],r['retrieval_status'],flush=True)
writecsv(EV/'downloads.csv',results,fields)
summary=dict(registered_routes=len(results),downloaded=sum(r['retrieval_status']=='downloaded' for r in results),pdf_files=sum(r['retrieval_status']=='downloaded' and r['local_path'].endswith('.pdf') for r in results),bytes=sum(int(r['bytes'] or 0) for r in results if r['retrieval_status']=='downloaded'),note='Downloaded files are not automatically relevant full texts or verified evidence.')
(EV/'download-summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary),flush=True)
