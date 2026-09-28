# Broncontrole en interpretatieaudit

De claimniveau-audit bevat 116 regels, één per geregistreerde claim. `source-audit.csv` onderscheidt primaire bron, passage, versie, toegang, interpretatie, scope en actualiteitsgrens. De classificatie MINOR bij een bronregel betekent beperkte restonzekerheid, niet automatisch een inhoudelijke fout. CRITICAL/MAJOR prioriteren risico voor de argumentatie.

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
