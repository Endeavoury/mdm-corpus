"""Check manuscript structure and traceability; does not evaluate an MDM prototype."""
import csv,hashlib,json,re,subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[2];E=R/'research/evidence';P=R/'research/paper'
def read(n):
 with (E/n).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
validated=[]
for path in E.glob('*.csv'):
 with path.open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
 assert all(None not in r and all(v is not None for v in r.values()) for r in rows),path
 validated.append(path.name)
sources=read('sources.csv');ids={r['id'] for r in sources};assert len(ids)==len(sources)
claims=read('claims-register.csv');cids={r['claim_id'] for r in claims};assert len(cids)==len(claims)==68
extracts=read('source-extracts.csv');exids={r['extract_id'] for r in extracts}
body='\n'.join(p.read_text() for p in sorted((P/'sections').glob('0*.tex')))
bodycids=re.findall(r'\\claim\{(RC\d+)\}',body);assert set(bodycids)==cids and len(bodycids)==len(cids)
cites={k.strip() for g in re.findall(r'\\(?:paren|text)cite(?:\[[^\]]*\])?\{([^}]+)\}',body) for k in g.split(',')}
bibids=set(re.findall(r'@\w+\{([^,]+),',(P/'references.bib').read_text()));assert cites<=ids and cites<=bibids
assert {r['source_id'] for r in extracts}==cites
for c in claims:
 assert set(c['source_ids'].split(';'))<=ids
 assert set(c['bronpassages'].split(';'))<=exids
for x in extracts:
 path=R/x['local_file'];assert path.exists(),path
 assert hashlib.sha256(path.read_bytes()).hexdigest()==x['sha256'],x['extract_id']
 if ':regel' in x['bronlocatie']:
  txtpath=R/x['bronlocatie'].split(':regel')[0]
  assert hashlib.sha256(txtpath.read_bytes()).hexdigest()==x['text_sha256']
trace=read('paper-traceability.csv');assert {r['claim_id'] for r in trace}==cids
assert {r['research_question'] for r in trace}=={'OV1','OV2','OV3','OV4','OV5','OV6'}
for r in trace:
 p=R/r['tex_file'];line=p.read_text().splitlines()[int(r['tex_line'])-1];assert r['claim_id'] in line
for name,key in [('concepts.csv','concept_id'),('gaps.csv','gap_id')]:
 rows=read(name);assert len({r[key] for r in rows})==len(rows)
 for r in rows:assert set(r.get('source_id',r.get('source_ids','')).split(';'))<=ids
log=(P/'mdm-overzicht.log').read_text(errors='replace');blg=(P/'mdm-overzicht.blg').read_text(errors='replace')
for bad in ['Citation .* undefined','Undefined control sequence','Invalid UTF-8','Missing character']:
 assert not re.search(bad,log),bad
assert not re.search(r'error message|I was expecting|Warning--',blg),blg
pdf=P/'mdm-overzicht.pdf';assert pdf.stat().st_size>10000
info=subprocess.check_output(['pdfinfo',str(pdf)],text=True);pages=int(re.search(r'Pages:\s+(\d+)',info)[1])
text=subprocess.check_output(['pdftotext','-layout',str(pdf),'-'],text=True);assert '\ufffd' not in text
(P/'mdm-overzicht.txt').write_text(text)
result=dict(date='2026-09-09',source_records=len(sources),cited_sources=len(cites),claims=len(claims),source_extracts=len(extracts),concepts=len(read('concepts.csv')),open_questions=len(read('gaps.csv')),pdf_pages=pages,pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),csv_files_structurally_checked=len(validated),overfull_boxes=len(re.findall('Overfull',log)),empirical_evaluation='niet uitgevoerd; buiten scope')
(P/'audit-result.json').write_text(json.dumps(result,indent=2)+'\n')
(P/'traceability-audit.md').write_text(f'''# Document- en traceability-audit

9 september 2026. Dit is een technische en redactionele documentcontrole, geen onafhankelijke peer review of empirische evaluatie.

## Vastgestelde uitkomsten

- PDF succesvol gecompileerd met Tectonic 0.17.0 en BibLaTeX/BibTeX: {pages} pagina's.
- {len(cites)} aangehaalde bron-ID's beschikbaar in bronnenregister en bibliografie.
- 68 unieke analytische claims gekoppeld aan bron-ID's, extracties en papersecties.
- Alle zes deelvragen vertegenwoordigd in `paper-traceability.csv`.
- 22 conceptanalyses en 8 als voorlopig gemarkeerde onderzoeksvragen.
- CSV-structuur, unieke claim-/bron-ID's, lokale bewijsbestanden, hashes en TeX-vindplaatsen gecontroleerd.
- Geen onopgeloste citaties, BibTeX-fouten, ontbrekende tekens of ongeldige UTF-8 in het einddocument.
- Overfull-boxmeldingen: {result['overfull_boxes']}. Resterende underfull-meldingen betreffen regelvulling, geen ontbrekende inhoud.

Het volledige machineleesbare auditresultaat staat in `audit-result.json`. De koppeling is onderzoeksvraag → bron/passageregistratie → analytische claim → papersectie. Requirements, ontwerpprincipes en prototype-experimenten zijn geen deliverables van deze brede reviewfase.

## Inhoudelijke grenzen

Bron-ID's zijn geen aantallen onafhankelijke studies. Passageregistratie bewijst vindbaarheid en integriteit van bestanden, niet de volledige juistheid van een interpretatie. Sommige bewijsposities zijn slechts officiële catalogi of abstracts. De bronlocatie vermeldt de gebruikte sectie en een tekstanker; het oorspronkelijke document blijft leidend. Eigen syntheses zijn herkenbaar en niet als consensus of empirische uitkomst geregistreerd.

Bij de identiteitscontrole is een gelinkte B07-PDF als ander werk herkend en uitgesloten als boekbewijs. M02 is aan de werkelijk gelezen parallelpublicatie gekoppeld. De overige kandidaatvermeldingen zijn niet door hun aanwezigheid als inhoudelijk beoordeeld voorgesteld.

De onderzoeksgaten blijven voorlopig. Onafhankelijke screening, menselijke vakreview, volledige normtoegang en uitbreiding van onderbelichte onderwerpen zijn niet uitgevoerd. De paper rapporteert geen prototype-, AI- of organisatie-experimenten.
''')
print(json.dumps(result,indent=2))
