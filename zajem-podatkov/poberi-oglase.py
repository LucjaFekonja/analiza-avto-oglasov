import re
import orodja

STEVILO_STRANI = 5000
STEVILO_OGLASOV_NA_STRAN = 20
stran = 0
mapa = 'zajem-podatkov\glavne-strani'
mapa_oglasov = 'zajem-podatkov\oglasi'

vzorec = (
    r'<a data-item-name="detail-page-link" href="(?P<url_oglasa>.*?)">\n'
    r'<div class="cldt-summary-title" id="cldt-ot-summary" data-test="listing-summary-title" data-item-name="headline">\n'
    r'<div class="cldt-summary-makemodelversion sc-ellipsis">\n'
    r'<h2 class="cldt-summary-makemodel sc-font-bold sc-ellipsis">(?P<avto>.*?)</h2>\n'
)

seznam_datotek_oglasov = list()
for page in range(STEVILO_STRANI):
    velikost = STEVILO_OGLASOV_NA_STRAN
    stran += 1
    url = f'https://www.autoscout24.com/lst/?sort=standard&desc=0&ustate=N%2CU&size={velikost}&page={stran}&atype=C&'
    datoteka = f'oglasi-stran-{stran}.html'
    orodja.shrani_stran(url, mapa, datoteka)
    vsebina = orodja.preberi_file(mapa, datoteka)

    for oglas in re.finditer(vzorec, vsebina):
        url_oglasa = 'https://www.autoscout24.com' + oglas.group('url_oglasa')
        ime_datoteke_oglasa = oglas.group('avto').lower().replace(' ', '-').replace('/', '-') + '.html'
        seznam_datotek_oglasov.append(ime_datoteke_oglasa)
        orodja.shrani_stran(url_oglasa, mapa_oglasov, ime_datoteke_oglasa)

