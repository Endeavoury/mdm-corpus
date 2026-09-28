"""Produce bibliography and requirement traceability from the frozen repository corpus."""
import csv,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent

def read(name):
    with (ROOT/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def esc(s):
    return ''.join({'&':r'\&','%':r'\%','_':r'\_','#':r'\#'}.get(c,c) for c in s)
sources=read('standards-matrix.csv'); literature=read('literature-matrix.csv')
bib=['% Alleen bronnen uit standards-matrix.csv en literature-matrix.csv.\n% Corpuspeildatum: 2026-09-07; gericht uitgebreid en gecontroleerd tijdens kritische review.\n']
for r in sources:
    urls=re.findall(r'https?://[^\s|;]+',r['primaire_bron'])
    fields={'author':'{'+esc(r['organisatie_eigenaar'])+'}', 'title':'{'+esc(r['standaard'])+'}', 'howpublished':esc(r['type_document']), 'url':urls[0] if urls else r['primaire_bron'], 'note':esc('Dossierreferentie '+r['id']+'. Versie: '+r['versie']+'. Bewijs: '+r['bewijsniveau']+'. Peildatum 7 september 2026.')}
    year_match=re.search(r'(?:19|20)\d{2}',r['versie']) or re.search(r'(?:19|20)\d{2}',r['status'])
    fields['year']=year_match.group(0) if year_match and r['id'] not in {'S40','S41','S48'} else 'z.d.'
    if len(urls)>1: fields['note']+=' Aanvullende primaire bronnen: '+'; '.join(r'\url{'+u+'}' for u in urls[1:])+'.'
    if r['id'] in {'S13','S14','S16','S22'}: fields['note'] += ' Lijststatus en toepassingsgebied: '+r'\url{'+r['bron_lijststatus']+'}.'
    if r['id']=='S19': fields['note'] += ' Nederlandse lijstversie 3.0 volgens het dossier; lijstbron: '+r'\url{'+r['bron_lijststatus']+'}.'
    bib.append('@misc{'+r['id']+',\n'+',\n'.join('  '+k+' = {'+v+'}' for k,v in fields.items())+'\n}\n')
for r in literature:
    author=r['auteur']
    if ' et al.' in author: author=author.split(' et al.')[0]+' and others'
    else: author=author.replace('; ',' and ')
    fields={'author':esc(author),'year':r['jaar'],'title':'{'+esc(r['titel'])+'}', 'howpublished':esc(r['publicatietype']), 'url':r['doi_of_stabiele_bron'],'note':esc('Dossierreferentie '+r['id']+'. Bewijs: '+r['bewijsniveau']+'.')}
    if 'doi.org/' in fields['url']: fields['doi']=fields['url'].split('doi.org/')[1]
    bib.append('@misc{'+r['id']+',\n'+',\n'.join('  '+k+' = {'+v+'}' for k,v in fields.items())+'\n}\n')
(ROOT/'references.bib').write_text('\n'.join(bib),encoding='utf-8')
# R01-R22 are preserved. R23 is an explicitly new design inference.
claims=read('claims-register.csv'); columns=list(claims[0])
new={
'claim_id':'R23','claim':'Maak epistemische categorie, gezagsgrond, afleidingswijze, bewijsstatus en modelversie afzonderlijk machineleesbaar per bewering.',
'claimtype':'ontwerpafleiding; onderzoekspropositie','bron_ids':'S25;S33;S04;L11;L16','primaire_bron':'; '.join(next(x['primaire_bron'] for x in sources if x['id']==k) for k in ['S25','S33','S04']),
'bronlocatie':'paper.tex: epistemische status; sections/architecture.tex: formeel metamodel',
'bewijs_samenvatting':'Bronnen ondersteunen onderscheid tussen gezag, herkomst en afleiding; de samengestelde classificatie en verplichte machineleesbaarheid zijn eigen ontwerpvoorstellen.',
'bewijsstatus':'Niet empirisch getoetste synthese; geen bestaand standaardprofiel',
'beperking_of_tegenbewijs':'Categorieën zijn niet onderling uitsluitend; expliciete metadata kan onjuist of onbewezen zijn. AI-effect onbekend.',
'eis_id':'R23','latere_toets':'T23/M23: deskundigenclassificatie en controle op onterechte verheffing van AI-afleiding tot authentiek gegeven; OV3, OV6; DP9; C1,C9,C15',
'geraadpleegd_op':'2026-09-07'}
if not any(r['claim_id']=='R23' for r in claims):claims.append(new)
# RQ, principles, architecture components, future metric name, concrete operationalization
spec=[
('OV2','DP1','C2;C3;C4;C5;C6','Typezuiverheid','Aandeel correct getypeerde knopen en relaties in een onafhankelijk beoordeelde steekproef; verwarringsmatrix per type.'),
('OV1;OV3','DP2','C1;C2;C9','Definitietraceerbaarheid','Volledig herleidbare definities / alle toepasselijke definities; bron, context, versie, verantwoordelijke en periode afzonderlijk scoren.'),
('OV3','DP3','C7','Identifierkwaliteit','Uniciteit binnen scope, persistentie over versies en correcte resolutie apart meten; nul verwisselingen tussen entiteit en document in kritieke taken.'),
('OV2;OV3','DP1','C5;C6','Elementdekking','Elementen met gevalideerde concept-, eigenschap- en domeinkoppeling / toepasselijke elementen.'),
('OV1;OV4','DP1;DP5','C6;C10;C13','Decodeerbaarheid','Correct gedecodeerde waarden / testwaarden; syntaxis, betekenisreferentie en dataspecificatie afzonderlijk beoordelen.'),
('OV3;OV5','DP4','C8;C11;C14','Temporele reconstructie','Correcte antwoorden op vooraf vastgestelde geldig-op/bekend-op-vragen / temporele vragen; publicatie- en eventtijd apart controleren.'),
('OV3;OV5','DP2;DP4','C9;C11','Provenancedekking','Beweringen met volledige bron- en afleidingsketen / beweringen waarvoor die keten vereist is; onbekend geldt als onvolledig.'),
('OV1;OV3','DP2;DP9','C1;C9;C13','Gezagsgetrouwheid','Juist geclassificeerde gezagsclaims / beoordeelde claims; aantal onterecht authentiek genoemde waarden afzonderlijk rapporteren.'),
('OV1;OV5','DP5','C10;C12','Kwaliteitsmetadata','Kwaliteitsmetingen met alle vereiste contextvelden / metingen; nauwkeurigheid van de waarden apart extern toetsen.'),
('OV3;OV5','DP3;DP7','C2;C4;C5;C6;C12;C13','Versie-impact','Precisie en recall van voorspelde afhankelijkheden tegenover handmatig gereviewde wijzigingen; reproduceerbaarheid van oude release.'),
('OV2;OV5','DP1;DP8','C3;C4;C5;C6','Mappingnauwkeurigheid','Precisie/recall van equivalente en niet-equivalente mappings tegen dubbel beoordeelde gouden standaard; onbekend apart houden.'),
('OV4;OV5','DP7','C1;C12;C14','Lifecyclevolledigheid','Toegestane statusovergangen met verantwoordelijke en besluitspoor / getoetste overgangen; ongeautoriseerde publicaties tellen.'),
('OV4;OV5','DP6','C12','Productcontractdekking','Aanwezige en inhoudelijk geldige contractvelden / toepasselijke velden; eigenaar en gebruiksdoel afzonderlijk scoren.'),
('OV1;OV5','DP6','C13','Interfaceconformiteit','Geslaagde toepasselijke profielcontroles / controles, uitgesplitst naar profielversie; semantische rondreis per representatie.'),
('OV3;OV5','DP7','C8;C14','Wijzigingsverwerking','Correcte eindtoestanden bij duplicaat-, volgorde- en herstelgevallen / scenario’s; detectie ontbrekende events en verwerkingstijd.'),
('OV2;OV5','DP5','C4;C10','Validatiezuiverheid','Precisie/recall van constraintdetectie; inferentie-uitkomsten en externe feitelijke juistheid als aparte uitkomsten rapporteren.'),
('OV6','DP6;DP9','C9;C12;C15','Machine-interpretatie','Correct beantwoorde betekenisvragen met geldige bronverwijzing / vragen; gepaste onthouding bij ontbrekend bewijs apart scoren.'),
('OV1;OV4','DP6','C1;C12;C13','FDStoepasselijkheid','Afspraken met gedocumenteerde toepasselijkheid en correcte bindendheidsclassificatie / geselecteerde toepasselijke afspraken.'),
('OV4;OV5','DP7','C1;C11;C14','Terugmeldtraceerbaarheid','Terugmeldscenario’s met bronhouder, status, beslissing en correctiespoor / scenario’s; doorlooptijd aanvullend meten.'),
('OV1;OV3','DP4;DP7','C9;C12','Bewaartraceerbaarheid','Als bewijs te bewaren objecten met passend metadata-profiel / geselecteerde bewaarobjecten; geen algemene MDTO-conformiteitsclaim.'),
('OV1;OV4','DP2','C1','Juridische toepasselijkheid','Door deskundige beoordeelde juiste scopebeslissingen / beslissingen; wettelijke plicht en profielkeuze afzonderlijk scoren.'),
('OV2;OV5','DP8','C3;C4;C5','Ontologische meerwaarde','Gedetecteerde identiteit/rol/fasefouten, fout-positieven en benodigde analistentijd; vergelijking met MIM-analyse zonder UFO.'),
('OV3;OV6','DP9','C1;C9;C15','Epistemische getrouwheid','Overeenstemming met deskundigen over categorie en gezagsgrond; nul onterechte opwaarderingen in kritieke scenario’s als voorgestelde acceptatiegrens.')]
rows=[]
reqs={r['claim_id']:r for r in claims if re.fullmatch(r'R\d+',r['claim_id'])}
for i,(q,dp,comp,name,op) in enumerate(spec,1):
    rid=f'R{i:02d}';r=reqs[rid]
    rows.append(dict(research_question=q,literature_and_standards=r['bron_ids'],requirement=rid,design_principle=dp,architecture_component=comp,proposed_evaluation_metric=f'M{i:02d}',test_id=f'T{i:02d}',metric_name=name,operationalization=op,evaluation_status='Voorgesteld; niet uitgevoerd'))
with (ROOT/'traceability-matrix.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
# Log design principles as original derivations with explicit limitations.
for i in range(1,10):
    key=f'DP{i}';linked=[r for r in rows if key in r['design_principle'].split(';')]
    src=sorted(set(k for r in linked for k in r['literature_and_standards'].split(';')))
    entry=dict.fromkeys(columns,'')
    entry.update(claim_id=key,claim=f'{key}: ontwerpprincipe zoals geformuleerd in sections/principles.tex; afgeleid uit '+', '.join(r['requirement'] for r in linked)+'.',claimtype='eigen ontwerpprincipe',bron_ids=';'.join(src),bronlocatie='sections/principles.tex',bewijs_samenvatting='Integratiesynthese van geregistreerde bronnen en requirements; geen letterlijke verplichting uit één norm.',bewijsstatus='Voorgesteld; empirische evaluatie nog uit te voeren',beperking_of_tegenbewijs='Bruikbaarheid, volledigheid en implementatiekosten niet vastgesteld.',eis_id=';'.join(r['requirement'] for r in linked),latere_toets=';'.join(r['proposed_evaluation_metric'] for r in linked),geraadpleegd_op='2026-09-07')
    if not any(r['claim_id']==key for r in claims):claims.append(entry)
for key,claim,src in [
('P01','De vijftienlaagse reference architecture en het getypeerde metamodel zijn een voorgestelde integratie; logische lagen impliceren geen verplichte fysieke services.','S13;S08;S31;S33;S47;L12'),
('P02','De verwachte meerwaarde van expliciete semantiek voor menselijke en AI-interpretatie is een te toetsen hypothese, geen empirisch resultaat van deze paper.','L11;L13;L16'),
('P03','De voorgestelde evaluatie vergelijkt dezelfde broninhoud met en zonder expliciete semantische koppelingen en gebruikt ablaties om mechanismen te onderscheiden.','L02;L03'),
('P04','Het lokale dossier ondersteunt een BAG-fragment, maar geen gevalideerde keten met BRP, BRK en WOZ; deze grens beperkt generaliseerbaarheid.','S49'),
('P05','De voorgestelde term semantic false agreement duidt hier op onterecht veronderstelde betekenisequivalentie; dit is een werkdefinitie, geen in het corpus geverifieerde afzonderlijke theorie.','S11;S31;L10'),
('P06','Een machineleesbare, getypeerde bewijs- en afhankelijkhedengraaf vormt de voorgestelde verbindende ontwerpbijdrage; nieuwheid buiten het corpus is niet vastgesteld.','L04;S08;S33;S47')]:
    entry=dict.fromkeys(columns,'');entry.update(claim_id=key,claim=claim,claimtype='ontwerpsynthese of afbakening',bron_ids=src,bronlocatie='paper.tex en sections/',bewijs_samenvatting='Eigen synthese op basis van het bestaande dossier; bronbeperkingen blijven gelden.',bewijsstatus='Voorstel; geen empirische evaluatie',beperking_of_tegenbewijs='Geen aanspraak op volledige literatuurdekking of bewezen effect.',latere_toets='Zie paper, evaluatie en traceability-matrix.csv',geraadpleegd_op='2026-09-07')
    if not any(r['claim_id']==key for r in claims):claims.append(entry)
# Store the actual principle statements and registered primary URLs, not only pointers.
source_urls={r['id']:r['primaire_bron'] for r in sources}
source_urls.update({r['id']:r['doi_of_stabiele_bron'] for r in literature})
principles=(ROOT/'sections/principles.tex').read_text() if (ROOT/'sections/principles.tex').exists() else ''
for r in claims:
    if re.fullmatch(r'DP[1-9]',r['claim_id']):
        match=re.search(r'\\textbf\{'+r['claim_id']+r'\.\} (.+)',principles)
        if match:r['claim']=r['claim_id']+': '+match.group(1)
    if r['claim_id'].startswith(('DP','P')):
        r['primaire_bron']='; '.join(source_urls[k] for k in r['bron_ids'].split(';') if k in source_urls)
with (ROOT/'claims-register.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=columns);w.writeheader();w.writerows(claims)
# Tables are generated to keep IDs, wording and citations aligned.
out=[r'\begin{longtable}{@{}P{.07\linewidth}P{.64\linewidth}P{.22\linewidth}@{}}',r'\caption{Afgeleide requirements. MOET betekent vereist binnen het voorgestelde ontwerp, niet zelfstandig wettelijk verplicht.}\label{tab:req}\\',r'\toprule Eis & Voorgestelde ontwerpverplichting & Grondslag \\ \midrule\endfirsthead',r'\toprule Eis & Voorgestelde ontwerpverplichting & Grondslag \\ \midrule\endhead']
for row in rows:
    r=reqs[row['requirement']]
    out.append(r'\hypertarget{'+row['requirement']+'}{}'+row['requirement']+' & '+esc(r['claim'])+' & '+r'\citep{'+','.join({'S46':'L11','S50':'L10'}.get(k,k) for k in r['bron_ids'].split(';'))+r'} \\')
out.append(r'\bottomrule\end{longtable}')
(ROOT/'sections/requirements-table.tex').write_text('\n'.join(out))
out=[r'\begin{longtable}{@{}P{.07\linewidth}P{.84\linewidth}@{}}',r'\caption{Voorgestelde meetcriteria; er zijn nog geen scores gemeten.}\label{tab:metrics}\\',r'\toprule ID & Operationalisering \\ \midrule\endfirsthead',r'\toprule ID & Operationalisering \\ \midrule\endhead']
for r in rows:out.append(r['proposed_evaluation_metric']+' & '+r'\textbf{'+esc(r['metric_name'])+'}. '+esc(r['operationalization'])+r' \\')
out.append(r'\bottomrule\end{longtable}');(ROOT/'sections/metrics-table.tex').write_text('\n'.join(out))
out=[r'\begin{longtable}{@{}P{.105\linewidth}P{.26\linewidth}P{.065\linewidth}P{.12\linewidth}P{.21\linewidth}P{.07\linewidth}@{}}',r'\caption{Expliciete auditketen: deelvraag, corpusbron, requirement, principe, component en toekomstige metriek. Bron-ID’s verwijzen naar de bibliografie en het dossier.}\label{tab:trace}\\',r'\toprule Vraag & Literatuur/standaard & Eis & Principe & Component & Toets \\ \midrule\endfirsthead',r'\toprule Vraag & Literatuur/standaard & Eis & Principe & Component & Toets \\ \midrule\endhead']
for r in rows:out.append(' & '.join(esc(r[k]).replace(';',r';\allowbreak{} ') for k in ['research_question','literature_and_standards','requirement','design_principle','architecture_component','proposed_evaluation_metric'])+r' \\')
out.append(r'\bottomrule\end{longtable}');(ROOT/'sections/traceability-table.tex').write_text('\n'.join(out))
print('Bibliography:',len(sources)+len(literature),'entries; requirements:',len(rows),'claims:',len(claims))
