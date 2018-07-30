# -*- coding: utf-8 -*-
import requests
import os.path
import csv

print 'Este Programa sirve para indentificar la implementación de una fuente de demanda (DSP) y su id correspondiente en una url.'
print 'Línea clasica de un adstxt: rubiconproject.com, 11438, RESELLER\nDonde "rubiconproject.com" es el nombre del DSP y "11438" el id.'
print 'Introduzca el nombre del DSP que debería estar implementado\nEjemplo: rubiconproject.com'
name_dsp = raw_input()
print 'Introduzca el id del dsp\nEjemplo: 16720'
id_dsp = raw_input()


class Adstxt:
    file_sites = 'sites.csv'
    url_a_analizar = []
    urls_analizadas = [['Sitio', 'Status']]
    sentencia = '/ads.txt'
    file = "Analisis.csv"

    def __init__(self):  # Sitios a evaluar
        if os.path.exists(self.file_sites):
            print 'Lista de sitios encontrada'
        else:
            print "Debe crear un .csv con los sitios a evaluar sin cabeceras llamado sites.csv.\nEjemplo:"
            print "cronista.com,\nclarin.com,\nlanacion.com.ar"
            exit()

    def chequeo_urls(self):  # Chequeamos que todas las urls queden sin una / en su terminación
        with open(self.file_sites, 'rb') as f:
            reader = csv.reader(f)
            reader = list(reader)  # Creamos lista de lista para evaluar individualmente cada URL

        for item in reader:
            for item in item:
                if "/" in item[-1:]:
                    base = []
                    item = item[:-1]
                    base.append(item)
                    self.url_a_analizar.append(base)
                else:
                    base = []
                    base.append(item)
                    self.url_a_analizar.append(base)

    def llamados_urls(self, dsp, dsp_id):
        for item in self.url_a_analizar:
            for item in item:
                try:
                    url = item + self.sentencia  # Agregamos la sentencia ads.txt a toda URL
                    r = requests.get(url)
                    r = r.text
                    # Buscamos la fuente específica que necesitamos
                    if dsp in r:
                        if dsp_id in r:
                            # Siempre que en el Ads.txt del sitio se encuentren los parametros dsp y dsp_id que ingresamos, el código estará bien implementado
                            base = []
                            base.append(item)
                            base.append('DSP bien implementado')
                            self.urls_analizadas.append(base)
                            print base
                        else:
                            # Si se encuentra el nombre del dsp pero no el ID nuestro el código no posee nuestro DSP
                            base = []
                            base.append(item)
                            base.append('No posee nuestro Adstxt')
                            self.urls_analizadas.append(base)
                            print base

                except requests.exceptions.ConnectionError:
                    # Casos en los que la URL no posea Adtxt
                    base = []
                    base.append(item)
                    base.append('Url sin adtxt')
                    self.urls_analizadas.append(base)
                    print base

        with open(self.file, "wb") as f:
            writer = csv.writer(f)
            writer.writerows(self.urls_analizadas)


Ejecutar = Adstxt()
Ejecutar.chequeo_urls()
Ejecutar.llamados_urls(name_dsp, id_dsp)
