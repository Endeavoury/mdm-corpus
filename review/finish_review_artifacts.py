import csv,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent

def read(n):
 with (ROOT/n).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(n,rows):
 with (ROOT/n).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
s=read('standards-matrix.csv');l=read('literature-matrix.csv');claims=read('claims-register.csv');trace=read('traceability-matrix.csv');src={r['id']:r for r in s+l}
# Explicit review of each requirement's inferential step, not an inference from ID coverage.
reason=[
('Rollen moeten voor beheerders en afnemers onderscheidbaar zijn; dat vereist geen universele resource-disjunctie.','Gedeelde resource met gedocumenteerde meervoudige typering','Iedere model-/conceptovergang','TP1','E1','RV05'),
('Een gezagsvraag kan alleen worden geadjudiceerd als definitie en context naar een controleerbare bron verwijzen.','Conventionele bronverwijzing en handmatige dossiercontrole','Uitspraak met normatieve of gezagsclaim','TP1;TP2','E1;E2','RV06'),
('Persistentie is een beleidseigenschap die niet door URI-syntax alleen wordt gerealiseerd.','Lokale sleutel met stabiele scope-/resolutietabel','Entiteit-, record- of versie-identificatie','TP1;TP4','E1;E4','RV07'),
('De gegevenselementmapping voegt interpretatie-informatie toe; het gebruik van een 11179-register is niet uniek noodzakelijk.','Goed gedocumenteerd conventioneel datadictionary','Data-element wordt tussen contexten uitgewisseld','TP1','E1','RV06'),
('Decodeerbaarheid wordt vereist als contractdoel; ISO-scope geldt uitsluitend voor relevante karakteristieke masterdataberichten.','Andere syntax met gelijkwaardige dataspecificatie','Toepasselijk bericht, niet alle interne data','TP1','E1','RV06'),
('Historische taken vragen twee expliciete tijdsperspectieven; OWL-Time is slechts een representatiekandidaat.','Bitemporele relationele tabellen','Historie-/correctietaak met beide tijdsbetekenissen','TP4','E4','RV09'),
('Afleidingsketens maken beoordeling mogelijk, maar provenance kan onjuist zijn en bewijst geen gezag.','Versiebeheerd log met dezelfde bron-/regelgegevens','Bewering waarvoor herkomst of afleiding relevant is','TP1;TP2;TP4','E1;E2;E4','RV18'),
('Authenticiteit, betrouwbaarheid en sender trust zijn verschillende beslissingen; hun scheiding is eigen profielbeleid.','Brongebonden gezagsbesluit in conventionele metadata','Positieve gezagsclaim of betwiste status','TP2','E2','RV18'),
('Een score zonder populatie en methode is niet vergelijkbaar; de gekozen verplichte contextvelden zijn ontwerpkeuze.','Kwaliteitsrapport met dezelfde context buiten de graaf','Gepubliceerde kwaliteitsmeting','TP1','E1','RV14'),
('Versieafhankelijkheden kunnen impactanalyse ondersteunen; meer afhankelijkheden kunnen onderhoudslast verhogen.','Zelfde versiearchief met handmatig bijgehouden releaseregister','Wijziging van gepubliceerd artefact','TP4','E4','RV20'),
('Motiveer een mapping om onterechte equivalentie te kunnen beoordelen; labels alleen zijn geen geldige goudstandaard.','Handmatig geadjudiceerde mappingtabel','Semantische/structurele grensvlakmapping','TP1;TP3','E1;E3','RV10'),
('Verantwoordelijke statusovergangen zijn governancekeuze; BOMOS schrijft niet deze volledige operationele lifecycle voor.','Bestaande workflow met beslislog','Publicatie, herziening of intrekking','TP4','E4','RV12'),
('Productcontractvelden moeten eerst op DCAT/DPROD worden gemapt; eigen metadata zijn alleen conditionele aanvulling.','Bestaand DPROD/DCAT-profiel zonder SMDP-uitbreiding','Beheerde productpublicatie','TP1','E1','RV01;RV07'),
('Profielconformiteit en semantische rondreis zijn aparte toetsen; een geslaagde interface voorspelt geen begrip.','OpenAPI plus conventionele contextlinks','Geselecteerd distributieprofiel','TP1','E1','RV13'),
('Eventenvelop adresseert niet alle domein-/herstelbetekenis; additionele regels hangen af van de afnemertaak.','Polling met versiearchief in plaats van events','Notificatie- of herstelbehoefte','TP4','E4','RV07'),
('Inferentie, graafconformiteit en werkelijkheid gebruiken verschillende toetsgronden.','SQL-/schemavalidatie plus aparte externe kwaliteitscontrole','Logische inferentie of constraintvalidatie','TP1','E1','RV14'),
('Machinebeschikbaarheid is geen gegarandeerd juist gebruik; betere toegang kan een rivaliserende verklaring zijn.','Zelfde context in conventioneel retrievalpakket','Automatische interpretatietaak','TP1;TP2','E1;E2','RV13'),
('FDS-afspraken zijn contextgebonden; toelatingsdekking is geen effectmetric.','Handmatige checklist met hetzelfde toepasselijkheidsbewijs','Voorgenomen FDS-toelating','TP1','E1','RV17'),
('Terugmeldingen moeten routeerbaar zijn; een eigen eventstack is niet noodzakelijk.','Bestaand terugmeldproces met versie-/besluitverwijzing','Betwist brongegeven met toepasselijke procedure','TP4','E4','RV20'),
('Bewaarmetadata zijn alleen relevant na expliciet bewaarbeleidsbesluit; geen generieke bewaarplicht afgeleid.','Los archiefdossier gekoppeld aan release','Als bewijs te bewaren objecten','TP4','E4','RV06'),
('Juridische toepasselijkheid vereist een deskundig contextbesluit; een complianceveld volstaat niet.','Gemotiveerd juridisch dossier buiten productgraaf','Mogelijk toepasselijke verplichting','TP1;TP2','E1;E2','RV17'),
('Ontologische verdieping is alleen kandidaat bij relevante categoriefouten; nut is kostenafhankelijk.','MIM-review met dezelfde expertise en taakset','Gedocumenteerde identiteit-/rol-/fasevraag','TP3','E3','RV08'),
('Registratie, productiemethode, onzekerheid en gezag zijn onafhankelijke profielvelden; PROV-O schrijft deze combinatie niet voor.','Conventioneel contextrecord met dezelfde annotaties','Uitspraak waarvoor bewijs- of gezagsstatus moet worden geïnterpreteerd','TP2','E2','RV18')]
rows=[]
for tr,(warrant,alt,when,tp,ex,rv) in zip(trace,reason):
 ids=tr['literature_and_standards'].split(';')
 if tr['requirement']=='R13':ids+=['S51']
 rows.append(dict(requirement=tr['requirement'],source_ids=';'.join(ids),source_locations=' | '.join(k+': '+src[k]['bronlocatie'] for k in ids),evidence_type='Conditionele ontwerpafleiding; bron ondersteunt bouwstenen/scope, geen causaal effect',inference_warrant=warrant,applicability=when,alternative=alt,counterevidence='Gelijkwaardig eenvoudiger alternatief, onjuiste broncontext of disproportionele kosten kan keuze weerleggen.',proposition=tp,experiment=ex,metric=tr['proposed_evaluation_metric'],metric_role='Contract-/componenttoets; comparatieve hoofdclaim vereist onafhankelijke taakuitkomst',reviewer_ids=rv,status='Afgeleid voorstel; empirisch niet getoetst'))
write('derivation-register.csv',rows)
# One claim-audit record per registered claim; source facts and own propositions are treated differently.
notes={
'S01':('MINOR','Editie-informatie opnieuw bekeken; boekinhoud niet gelezen.','Editie bevestigd; inhoudelijke boekclaims niet gedragen.'),
'S03':('MAJOR','ISO-catalogusabstract opnieuw gelezen; scope en uitsluitingen gecontroleerd.','Geen clausuleconformiteit of generieke interne MDM-plicht afleiden.'),
'S08':('MAJOR','ISO-catalogusabstract opnieuw gelezen: data elements, concepts, domains en derivation rules.','Geen universele MIM-mapping of fysiek opslagmodel gegeven.'),
'S13':('MAJOR','Primaire MIM §1.6 en lijstpagina gelezen; 1.2 aanbevolen.','Begrip-woordgebruik verschilt; conceptueel/logisch/technisch niet samenvoegen.'),
'S14':('MINOR','NL-SBB 1.0 specificatie en lijstpagina gecontroleerd.','Pas toe of leg uit vanaf 2026-01-01 binnen scope; geen automatisch juridisch juist handelen.'),
'S15':('MINOR','TOOI downloads en Forum-procedurepagina bekeken.','Ontologierelease, documentrelease en lijstprocedure hebben eigen versie/status; geen volledige Stelselontologie.'),
'S16':('MINOR','Vastgestelde NL-publicatie en lijstpagina gecontroleerd.','Lijstpagina in behandeling; geen eigen conclusie over latere besluitvorming.'),
'S17':('MAJOR','NEN-catalogus en Geo-lijstbron opnieuw bekeken; volledige norm niet gelezen.','Scope-/editiecontrole; geen conformiteitsverklaring.'),
'S19':('MINOR','Technische 3.1.1-referentie en Forum-lijstpagina gecontroleerd.','Lijstveld 3.0 met 3.1-procedure; technische referentie niet automatisch lijstverplichting.'),
'S20':('MINOR','Algemene URL is een clientredirect; doel /4.0.1/ apart opgehaald, Forum-scope bekeken.','Geen complete familieconformiteit gecontroleerd; normatief detail vereist afzonderlijke profieltoets.'),
'S21':('MINOR','FSC Core 2.0.0 geselecteerde publicatie en via Digikoppeling lijstcontext bekeken.','Afzendervertrouwen impliceert geen authentieke inhoud.'),
'S22':('MINOR','Logius 1.1 en Forum-versieveld gecontroleerd; linklabel noemt nog 1.0.','Pagina-inconsistentie geregistreerd, niet stilzwijgend opgelost.'),
'S24':('MINOR','Nationaal Archief-overzicht onderscheidt normerende en niet-normerende delen.','Geen volledige modulaire conformiteit gecontroleerd; conditionele bewaartoepassing.'),
'S25':('MINOR','Historisch Kamerstuk met twaalf eisen als beleidstekst gecontroleerd.','Geen actuele attributen- of verwerkingsbevoegdheid uit historisch overzicht afleiden.'),
'S26':('MINOR','Baseline-PDF met bestaande en potentiële afspraken onderzocht.','Potentiële afspraken niet als vastgesteld presenteren.'),
'S27':('MINOR','FDS v1 tabel en bindingen bekeken, inclusief aanbevolen KW001.','Versielabel garandeert geen immutable webinhoud; geen algemene wettelijke plicht.'),
'S31':('MAJOR','SKOS §3.5.1 expliciet gecontroleerd.','Concept/klasse-dubbeltypering toegestaan; eigen rolonderscheid geen standaarddisjunctie.'),
'S33':('MAJOR','PROV-O begrippen en qualified patterns gecontroleerd.','Provenance-uitdrukbaarheid bewijst geen bronwaarheid of kant-en-klare epistemische classificatie.'),
'S34':('MINOR','DQV-publicatiestatus en kwaliteitsmetingconcepten bekeken.','Working Group Note, geen Recommendation of zelfstandig kwaliteitsbewijs.'),
'S37':('MINOR','Expliciet gedateerde Recommendation 2017 gebruikt.','Geen claim dat elke latere versie dezelfde status heeft; geen automatisch bitemporeel protocol.'),
'S40':('MINOR','UFO-communitypagina en academische antecedenten gebruikt.','Geen algemeen release- of Nederlandse standaardenstatus afgeleid.'),
'S41':('MINOR','Communitydocumentatie en L09 abstract bevestigen ontologische modelleringspositionering.','Geen noodzakelijkheid of Nederlands overheidsstandaardlabel.'),
'S42':('MINOR','Primaire verordening, scope en artikel 3-context gecontroleerd.','Geen algemene OWL/RDF-verplichting; concrete juridische beoordeling ontbreekt.'),
'S44':('MINOR','Vier afzonderlijke SEMIC-releasepagina’s opgehaald en scope bekeken.','Geen familieversie of automatische Nederlandse juridische equivalentie.'),
'S49':('MAJOR','Officiële cataloguspublicatiepagina opnieuw bekeken.','BAG-fragmentkeuze ondersteund; geen feitelijke cross-registry mapping of juridisch gevalideerde casus.'),
'S51':('MAJOR','OMG Beta1-cover, product/dataservice-secties en catalogus gecontroleerd.','Relevante overlap; beta-status en geen casus-effectbewijs.'),
'L03':('MAJOR','Uitgeversbibliografie opnieuw gevonden; directe PDF/DOI-toegang geweigerd.','Bibliografie bevestigd; methodologische inhoud niet opnieuw volledig geverifieerd. Oorspronkelijk abstractniveau blijft grens.'),
'L06':('MINOR','Institutioneel bibliografisch record; geen inhoudelijke bronbevinding.','Niet aangehaald voor onderzoeksresultaten.'),
'L09':('MINOR','Oorspronkelijke institutionele route geeft slechts applicatiescherm; alternatief primair uitgeversabstract gelezen.','Abstract ondersteunt UFO/OntoUML-positionering; geen lokale meerwaarde.'),
'L18':('CRITICAL','Primaire VLDB-PDF, abstract en architectuursecties gecontroleerd.','Direct antecedent dwingt afzwakking brede noveltyclaim.'),
'L19':('MAJOR','Primaire uitgeverstekst, model en meetvoorbeeld bekeken.','Kwaliteitsoperationalisering is bestaand werk; geen SMDP-validatie.')}
source_rows=[]
for r in claims:
 ids=re.findall(r'\b[SL]\d{2}\b',r['bron_ids'])
 if r['claim_id'].startswith('C-'):
  sid=r['claim_id'][2:];b=src[sid]
  sev,checked,limit=notes.get(sid,('MINOR','Primaire geregistreerde bronroute en relevante scope-/abstractpassages gecontroleerd; geen volledige clausuleaudit.','Ondersteunt alleen de geregistreerde scope/bevinding, geen SMDP-effect.'))
  if sid in [f'S{i:02}' for i in range(2,13)] and sid not in notes:checked='Officiële ISO-catalogus via webtool geopend; editie, abstract en scope gecontroleerd; volledige norm niet gelezen.';limit='Geen clausuleconformiteit; interpretatie beperkt tot publiek abstract.'
  access='Beperkt tot editie/scope/abstract' if sid in {f'S{i:02}' for i in range(1,13)}|{'S17','L03','L05','L06','L08','L09','L15','L16','L17'} else 'Relevante primaire passages; geen integrale conformiteitsaudit'
  if sid=='L03':access='Onopgelost voor inhoudelijke herverificatie; bibliografie bevestigd'
  urls=b.get('primaire_bron',b.get('doi_of_stabiele_bron',''));loc=b['bronlocatie'];version=b.get('versie',b.get('jaar',''))
  actual='Geselecteerde bronversie gecontroleerd; geen uitputtende zoektocht naar alle opvolgversies'
 else:
  sev='MAJOR' if r['claim_id'].startswith(('R','DP','TP','G')) else 'MINOR';checked='Afleiding beoordeeld tegen bron-scope en expliciete tegenargumenten; geen directe bron-entailment geclaimd.';limit='Eigen ontwerpkeuze/hypothese of lokale observatie; empirische validatie ontbreekt.';access='Geen extern effectbewijs; zie bronclaims van bron_ids';urls=' | '.join(src[k].get('primaire_bron',src[k].get('doi_of_stabiele_bron','')) for k in ids);loc=r['bronlocatie'];version='Profielvoorstel, revisie 2026-09-07';actual='Geen feitelijke actuele normstatus geclaimd door deze ontwerpafleiding'
  if r['claim_id']=='G01':sev='CRITICAL';limit='Brede noveltyclaim vervalt; restvraag blijft voorlopig en niet systematisch als gap bewezen.'
 source_rows.append(dict(claim_id=r['claim_id'],claim=r['claim'],source_ids=r['bron_ids'],primary_source=urls,source_location=loc,selected_version=version,access_and_evidence=access,interpretation_check=checked,scope_limit=limit,currency_check=actual,severity=sev,checked_on='2026-09-07',verification_boundary='Bron-/ontwerpcontrole; geen prototype-evaluatie'))
write('source-audit.csv',source_rows)
(ROOT/'source-audit.md').write_text(f'''# Broncontrole en interpretatieaudit

De claimniveau-audit bevat {len(source_rows)} regels, één per geregistreerde claim. `source-audit.csv` onderscheidt primaire bron, passage, versie, toegang, interpretatie, scope en actualiteitsgrens. De classificatie MINOR bij een bronregel betekent beperkte restonzekerheid, niet automatisch een inhoudelijke fout. CRITICAL/MAJOR prioriteren risico voor de argumentatie.

De oorspronkelijke fetch controleerde 91 URL-routes; 73 leverden via de lokale HTTP-client inhoud. Dit is een bereikbaarheidslog, geen lees- of conformiteitsbewijs. De overige ISO-catalogi zijn via de webtool geopend. Alternatieve uitgeversroutes voor FEDS en UFO zijn afzonderlijk nagegaan. FEDS blijft voor inhoudelijke herverificatie open; de bibliografie is bevestigd. Drie relevante tegenbronnen zijn apart geregistreerd als S51, L18 en L19.

## Materiële correcties

1. **CRITICAL — novelty:** [SMDM (2009)](https://www.vldb.org/pvldb/vol2/vldb09-1011.pdf) is een directe voorganger. De brede nieuwheidsclaim is vervangen door een vergelijkingsvraag.
2. **MAJOR — productmetadata:** [DPROD Beta 1](https://www.omg.org/spec/DPROD/1.0/Beta1/PDF) maakt hergebruik/vergelijking noodzakelijk vóór een eigen productschema wordt voorgesteld.
3. **MAJOR — typegrenzen:** [SKOS §3.5.1](https://www.w3.org/TR/skos-reference/#notes) staat concept/klasse-dubbeltypering toe. Het paperprofiel onderscheidt beheerrollen en beweert geen universele disjunctie.
4. **MAJOR — woordgebruik:** [MIM §1.6](https://docs.geostandaarden.nl/mim/def-st-mim-20240613/) gebruikt begrip anders dan het afzonderlijke beheer van term, definitie en concept. Het verschil is nu expliciet.
5. **MAJOR — inferentiesprong:** [ISO 8000-110](https://www.iso.org/standard/78501.html) ondersteunt scope voor specifieke uitwisselberichten; niet alle interne producteisen. [ISO/IEC 11179-31](https://www.iso.org/standard/78925.html) ondersteunt registratiemetadata, geen unieke implementatiearchitectuur.
6. **MINOR — lijststatus:** NL-SBB 1.0, MIM 1.2, DCAT-AP-NL 3.0 en OpenAPI lijstversie 3.0 zijn rechtstreeks aan Forum-pagina’s getoetst. CloudEvents heeft een 1.1-versieveld met 1.0-linklabel; deze inconsistentie blijft zichtbaar.

## Resterende grenzen

- Volledige DAMA-DMBOK-, ISO- en NEN-inhoud is niet integraal gelezen. Scopebevestiging is geen normconformiteit.
- Sommige academische claims blijven op abstractniveau. De audit vult geen ontbrekende auteurs, DOI’s of paginanummers in.
- Vastgezette referentieversies zijn niet per definitie de allernieuwste release; actualiteit is geen onbeperkte monitorclaim.
- Normatieve bronbeschrijvingen en adoptieverwachtingen zijn geen empirisch effectbewijs. Dat geldt ook als een officiële lijstpagina een sterk geformuleerd voordeel vermeldt.
- Het juridische gezag van concrete BAG/BRP/BRK/WOZ-attributen is niet vastgesteld. De casus blijft begrensd.
- Alle R-, DP- en TP-claims zijn afleidingen/voorstellen. Traceability bevestigt hun verbindingen, niet hun waarheid of effect.
- Deze audit en review zijn door dezelfde AI-assistent uitgevoerd, niet door externe onafhankelijke vakexperts.
''')
# Update response execution status; distinguish editorial closure and unresolved empirical requirements.
responses=read('reviewer-response-matrix.csv')
paths={'RV01':'sections/introduction.tex','RV02':'sections/pre-evaluation.tex','RV03':'sections/theory.tex','RV04':'sections/theory.tex','RV05':'sections/theory.tex; sections/architecture.tex','RV06':'derivation-register.csv; sections/principles.tex','RV07':'sections/architecture.tex','RV08':'sections/principles.tex; sections/evaluation-design.tex','RV09':'sections/architecture.tex','RV10':'sections/integration-decisions.tex','RV11':'paper.tex; sections/introduction.tex','RV12':'derivation-register.csv; sections/derivation-table.tex','RV13':'sections/evaluation-design.tex','RV14':'sections/case-evaluation.tex; derivation-register.csv','RV15':'sections/evaluation-design.tex; sections/pre-evaluation.tex','RV16':'sections/case-evaluation.tex; sections/discussion.tex','RV17':'sections/integration-decisions.tex; source-audit.csv','RV18':'sections/architecture.tex; claims-register.csv','RV19':'sections/case-evaluation.tex; sections/discussion.tex','RV20':'sections/architecture.tex; sections/discussion.tex','RV21':'sections/pre-evaluation.tex; traceability-audit.md','RV22':'source-audit.csv; source-audit.md','RV23':'sections/pre-evaluation.tex','RV24':'sections/cross-standard-table.tex; paper.tex','RV25':'derivation-register.csv; sections/derivation-table.tex','RV26':'source-audit.csv; references.bib'}
for r in responses:
 r['gewijzigde_papersectie']=paths[r['reviewer_id']]
 r['uitvoeringsstatus']='Tekst/ontwerp herzien; empirische toets nog niet uitgevoerd'
 if r['reviewer_id'] in ['RV01','RV11','RV16','RV22','RV23']:r['uitvoeringsstatus']='Afbakening en plan herzien; inhoudelijke/empirische open punten blijven expliciet'
write('reviewer-response-matrix.csv',responses)
md='# Reviewer-response matrix\n\nBeslissingen betreffen de 26 commentaren op de bewaarde ingediende versie. Acceptatie van een commentaar betekent geen afgeronde empirische validatie.\n\n'
for r in responses:md+=f"## {r['reviewer_id']} — {r['severity']} — {r['besluit']}\n\n**Commentaar:** {r['reviewer_comment']}\n\n**Beoordeling:** {r['beoordeling']}\n\n**Wijziging:** {r['voorgestelde_wijziging']}\n\n**Rationale:** {r['rationale']}\n\n**Gewijzigd:** {r['gewijzigde_papersectie']}\n\n**Status:** {r['uitvoeringsstatus']}\n\n"
(ROOT/'reviewer-response-matrix.md').write_text(md)
# Complete requirement-to-experiment appendix: evidence IDs remain in the existing traceability table.
tex=[r'\begin{longtable}{@{}P{.07\linewidth}P{.47\linewidth}P{.23\linewidth}P{.15\linewidth}@{}}',r'\caption{Aanvullende traceability: eigen inferentiestap, alternatief en toekomstige experimenten. Alle bronlocaties staan in het derivation-register.}\\',r'\toprule Eis & Aanvullende ontwerpaanname & Concurrerend alternatief & Propositie / test \\ \midrule\endfirsthead',r'\toprule Eis & Aanvullende ontwerpaanname & Concurrerend alternatief & Propositie / test \\ \midrule\endhead']
def esc(v):return v.replace('&',r'\&').replace('%',r'\%').replace('_',r'\_')
for r in rows:tex.append(' & '.join(esc(v) for v in [r['requirement'],r['inference_warrant'],r['alternative'],r['proposition'].replace(';',', ')+r'\newline '+r['experiment'].replace(';',', ')])+r' \\')
tex.append(r'\bottomrule\end{longtable}')
(ROOT/'sections/derivation-table.tex').write_text('\n'.join(tex))
print('Artifacts written:',len(source_rows),'claim audits;',len(rows),'derivations;',len(responses),'responses')
