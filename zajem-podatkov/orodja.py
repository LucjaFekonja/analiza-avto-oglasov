import csv
import json
import os
import requests


def url_v_niz(url):
    ''' Sprejme niz (url), vrne vsebino spletne strani kot niz '''
    try:
        odziv = requests.get(url)                   # Če je odziv 200, ne potrebuje exceptiona
    except requests.exceptions.ConnectionError:
        print('Napaka pri povezovanju do:', url)    # Če pride do napake pri povezovanju
        return None
    
    if odziv.status_code == requests.codes.ok:      # Če ni bilo errorja
        return odziv.text                           # Vrne vsebino spletne strani
    else:
        print('Napaka pri prenosu strani:', url)


def niz_v_file(niz, mapa, datoteka):
    ''' niz pretvori v datoteko in so shrani v mapo, če že obstaja, naredi novo'''
    os.makedirs(mapa, exist_ok=True)      
    path = os.path.join(mapa, datoteka)    # Ustvari path do datoteke v katero shranjujemo
    with open(path, 'w', encoding='utf-8') as dat:
        dat.write(niz)                     # V datoteko vpiš niz
    return None


def shrani_stran(url, mapa, datoteka):
    ''' Vrne vsebino datoteke kot niz '''
    niz = url_v_niz(url)
    niz_v_file(niz, mapa, datoteka)
    return None


def preberi_file(mapa, datoteka):
    path = os.path.join(mapa, datoteka)
    with open(path, 'r', encoding='utf-8') as dat:
        return dat.read()
