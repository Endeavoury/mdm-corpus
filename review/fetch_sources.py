"""Read-only retrieval log. Successful retrieval is not semantic verification."""
import csv,concurrent.futures,hashlib,urllib.request,re,datetime,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
OUT=Path('/tmp/paper-review-sources');OUT.mkdir(exist_ok=True)
rows=[]
for name in ['standards-matrix.csv','literature-matrix.csv']:
 for r in csv.DictReader((ROOT/name).open(encoding='utf-8-sig')):
  fields=['primaire_bron','bron_lijststatus'] if r['id'].startswith('S') else ['doi_of_stabiele_bron','bronlocatie']
  for field in fields:
   for n,u in enumerate(re.findall(r'https?://[^\s|;]+',r[field])):
    rows.append((r['id'],field,n,u))
def get(item):
 sid,kind,n,url=item
 rec=dict(source_id=sid,source_role=kind,url=url,checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),http_status='',resolved_url='',sha256='',bytes=0,local_snapshot='',retrieval_result='')
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (academic source verification)'})
  with urllib.request.urlopen(req,timeout=18) as r:
   data=r.read(12000000);rec.update(http_status=r.status,resolved_url=r.url,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))
   ext='pdf' if data.startswith(b'%PDF') else 'html'
   path=OUT/f'{sid}-{kind}-{n}.{ext}';path.write_bytes(data);rec.update(local_snapshot=str(path),retrieval_result='retrieved; interpretation requires separate review')
 except Exception as ex:rec['retrieval_result']=str(ex)
 return rec
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
 result=list(pool.map(get,rows))
with (ROOT/'review/source-fetch.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(result[0]));w.writeheader();w.writerows(result)
print('retrieved',sum(bool(r['sha256']) for r in result),'of',len(result))
for r in result:
 if not r['sha256']:print(r['source_id'],r['source_role'],r['retrieval_result'])
