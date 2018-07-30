#!/usr/bin/env python

"""
Script para capturar el ranking que ofrece Alexa a una url
"""

import urllib
import bs4

url = ['zocalo.com.mx', '107.0.22.34', 'aaaaasdasdsd', 'clarin.com']  # Distintas URLs
url_2 = [['Url', 'Global Ranking', 'Geo', 'Geo_ranking']]

for item in url:
    data = []
    url = bs4.BeautifulSoup(urllib.urlopen("http://data.alexa.com/data?cli=10&dat=s&url={}".format(item)).read(), "xml")
    if url.find('COUNTRY'):
        w_rank = url.find("REACH")['RANK'].encode("utf-8")
        g_code = url.find("COUNTRY")['CODE'].encode("utf-8")
        r_rank = url.find("COUNTRY")['RANK'].encode("utf-8")
        data.append(item)
        data.append(w_rank)
        data.append(g_code)
        data.append(r_rank)
        url_2.append(data)
    else:
        pass

print url_2
