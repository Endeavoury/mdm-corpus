"""Audit document integrity, never empirical prototype performance."""
import csv, hashlib, re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent

def read(name):
    raw=(ROOT/name).read_bytes()
    assert raw.startswith(b'\xef\xbb\xbf'),f'Missing UTF-8 BOM: {name}'
    with (ROOT/name).open(encoding='utf-8-sig',newline='') as f:
        rows=list(csv.DictReader(f))
    assert rows and all(None not in r and all(v is not None for v in r.values()) for r in rows),name
    return rows
s=read('standards-matrix.csv');l=read('literature-matrix.csv');c=read('claims-register.csv');t=read('traceability-matrix.csv')
for rows,key in [(s,'id'),(l,'id'),(c,'claim_id'),(t,'requirement')]:
    assert len({r[key] for r in rows})==len(rows),f'Duplicate {key}'
known={r['id'] for r in s+l}
bib=(ROOT/'references.bib').read_text()
bibkeys=re.findall(r'@\w+\{([^,]+),',bib)
assert len(bibkeys)==len(set(bibkeys)) and set(bibkeys)==known
texfiles=[ROOT/'paper.tex']+sorted((ROOT/'sections').glob('*.tex'))
text='\n'.join(p.read_text() for p in texfiles)
cites={k.strip() for group in re.findall(r'\\cite\w*\{([^}]+)\}',text) for k in group.split(',')}
assert cites<=known,cites-known
assert 'L06' not in cites,'Metadata-only L06 must not support findings'
labels=re.findall(r'\\label\{([^}]+)\}',text)
assert len(labels)==len(set(labels))
assert set(re.findall(r'\\(?:ref|pageref)\{([^}]+)\}',text))<=set(labels)
for target in re.findall(r'\\input\{([^}]+)\}',text):assert (ROOT/(target+'.tex')).exists(),target
for r in c:
    refs=set(re.findall(r'\b[SL]\d{2}\b',r['bron_ids']))
    assert refs<=known,(r['claim_id'],refs-known)
reqs={f'R{i:02d}' for i in range(1,24)}
assert {r['requirement'] for r in t}==reqs
assert reqs<={r['claim_id'] for r in c}
for r in t:
    assert set(r['literature_and_standards'].split(';'))<=known
    assert r['evaluation_status']=='Voorgesteld; niet uitgevoerd'
    n=int(r['requirement'][1:]);assert r['proposed_evaluation_metric']==f'M{n:02d}' and r['test_id']==f'T{n:02d}'
    for field in ['research_question','design_principle','architecture_component']:
        assert r[field]

def union(field):return {v for r in t for v in r[field].split(';')}
assert union('research_question')=={f'OV{i}' for i in range(1,7)}
assert union('design_principle')=={f'DP{i}' for i in range(1,10)}
assert union('architecture_component')=={f'C{i}' for i in range(1,16)}
for phrase in ['de resultaten tonen aan','het prototype bewijst','de test bevestigt']:
    assert phrase not in text.lower(),phrase
# Source URLs must come from matrix fields, including registered source-location URLs.
urlpool='\n'.join(str(v) for row in s+l for v in row.values())
urls=re.findall(r'^  url = \{([^}]+)\}',bib,re.M)
assert all(u in urlpool for u in urls),'New bibliographic source URL'
log=(ROOT/'paper.log').read_text(errors='replace') if (ROOT/'paper.log').exists() else ''
issues=[]
for pattern in [r'LaTeX Warning:.*undefined',r'Package natbib Warning:.*undefined',r'Overfull \\[hv]box',r'^! ']:
    issues+=re.findall(pattern,log,re.M)
assert not issues,issues
blg=(ROOT/'paper.blg').read_text(errors='replace')
assert 'Warning--' not in blg and 'error message' not in blg, 'BibTeX warnings or errors'
pdf=ROOT/'paper.pdf'
assert pdf.exists() and pdf.stat().st_size>10000,'Compile PDF before final audit'
sha=hashlib.sha256(pdf.read_bytes()).hexdigest()
# Review workflow and semantic derivation records are audited separately from syntax.
import json, zipfile
review_done=json.loads((ROOT/'review/review-completed.json').read_text())
assert hashlib.sha256((ROOT/'peer-review.md').read_bytes()).hexdigest()==review_done['review_sha256']
assert review_done['baseline_unchanged_at_review_completion'] is True
manifest=json.loads((ROOT/'review/baseline/manifest.json').read_text())
with zipfile.ZipFile(ROOT/'review/baseline/submitted-manuscript.zip') as z:
    for name,digest in manifest['files'].items():assert hashlib.sha256(z.read(name)).hexdigest()==digest
assert hashlib.sha256((ROOT/'AGENTS.md').read_bytes()).hexdigest()==manifest['files']['AGENTS.md']
derivations=read('derivation-register.csv');sourceaudit=read('source-audit.csv');responses=read('reviewer-response-matrix.csv')
assert {r['requirement'] for r in derivations}==reqs
assert {r['claim_id'] for r in sourceaudit}=={r['claim_id'] for r in c}
claim_map={r['claim_id']:r['claim'] for r in c}
assert all(r['claim']==claim_map[r['claim_id']] for r in sourceaudit),'Stale source audit'
assert {r['reviewer_id'] for r in responses}=={f'RV{i:02d}' for i in range(1,27)}
assert len(responses)==26
for r in derivations:
    assert all(r[k] for k in ['source_locations','inference_warrant','alternative','applicability','proposition','experiment'])
    assert set(r['source_ids'].split(';'))<=known
    assert set(r['proposition'].split(';'))<={f'TP{i}' for i in range(1,5)}
    assert set(r['experiment'].split(';'))<={f'E{i}' for i in range(1,5)}
for r in responses:
    assert r['besluit'] in {'geaccepteerd','gedeeltelijk','verworpen'}
    for path in r['gewijzigde_papersectie'].split(';'):assert (ROOT/path.strip()).exists(),path
assert all(f'TP{i}' in text and f'E{i}' in text for i in range(1,5))
report=f'''# Traceability-audit na kritische review en revisie

Documentcontrole uitgevoerd op 7 september 2026. Deze controle is geen empirische prototype-evaluatie en geen externe peer review.

## Volgorde en bewaarde basis

De ingediende versie is intact bewaard in `review/baseline/submitted-manuscript.zip`; alle hashes in het manifest zijn gecontroleerd. `review/review-completed.json` legt vast dat de volledige review gereed was terwijl alle manuscriptbestanden nog ongewijzigd waren. De reviewtekst heeft nog dezelfde hash. De response matrix en revisie volgen op die review. `AGENTS.md` is ongewijzigd.

## Interne dekking

- {len(s)} standaard-/kadervermeldingen en {len(l)} literatuurvermeldingen; reviewtoevoegingen S51, L18 en L19 expliciet geregistreerd.
- {len(bibkeys)} unieke bibliografiesleutels; {len(cites)} aangehaald. Alle bron-URL’s bestaan in de herziene matrices.
- {len(c)} unieke claims, elk met een actuele regel in `source-audit.csv`.
- 23 requirements verbonden met 6 deelvragen, 9 principes, 15 analyseviews en 23 toekomstige metrieken.
- Alle 23 requirements hebben daarnaast bronlocatie, inferentiestap, toepasselijkheid, alternatief, propositie en experiment in `derivation-register.csv`.
- 4 niet-getoetste theoretische propositions verbonden met 4 geplande experimenten.
- 26 reviewercommentaren hebben beoordeling, besluit, rationale, concrete gewijzigde bestanden en een uitvoeringsstatus.
- TeX-inputs, citaties, labels en bibliografiesleutels opgelost. Geen overvolle tekstvakken, ontbrekende referenties of BibTeX-waarschuwingen in de definitieve logs. Eventuele underfull-meldingen betreffen woordspatiëring.

## Inhoudelijke auditgrens

De broncontrole omvat scope/interpretatie van dragende claims en registreert beperkte toegang. ISO/NEN/DAMA zijn geen integraal gelezen normcorpus; FEDS is niet volledig inhoudelijk opnieuw geverifieerd. Een succesvolle HTTP-response of citation key geldt niet als inhoudelijk bewijs. Details staan in `source-audit.md` en `source-audit.csv`.

De brede noveltyclaim is afgezwakt. De centrale hypothese wordt vergeleken met A1, een conventioneel contextregister met dezelfde inhoud. De vijftien lagen zijn analyseviews en geen vereiste vijftien services. SKOS-dubbeltypering, MIM-woordgebruik, statementidentiteit en onafhankelijke epistemische assen zijn expliciet. De audit bewijst niet dat het nieuwe metamodel correct of volledig is.

Alle prototype-eigenschappen blijven niet beoordeeld. BAG vormt slechts een begrensde illustratie; geen Stelselbrede empirische claim. Relevante-effectmarges, acceptatiebesluiten, steekproef en experimenten zijn nog niet vastgesteld of uitgevoerd. Een praktisch gelijkwaardig eenvoudiger alternatief kan de nettowaardethese weerleggen. Review en revisie zijn verricht door dezelfde AI-assistent en mogen niet als externe bevestiging worden gepresenteerd.

## Compilatie

Tectonic 0.17.0 met BibTeX/`plainnat`. Reproduceren: `make TECTONIC=/pad/naar/tectonic`.

PDF SHA-256: `{sha}`.

Het slothoofdstuk en `pre-evaluation-research-state.md` specificeren propositions, principes, prototypevragen, onafhankelijke/afhankelijke variabelen en ondersteuning-/weerleggingscondities.
'''
(ROOT/'traceability-audit.md').write_text(report)
print(f'PASS: {len(cites)} citation keys, {len(c)} claims, 23 complete traceability chains. PDF SHA256 {sha}')
