# Script para determinar la categoria de una url utilizando bluecoat!

import json
import requests

listatotal = [['URL', 'Category']]
url = ['889noticias.mx']
for item in url:
    lista = []
    baseurl = "https://sitereview.bluecoat.com/resource/lookup"
    headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
    payload = {"url": item, "captcha": ""}
    req = requests.post(baseurl, headers=headers, data=json.dumps(payload))
    response = json.loads(req.content.decode("UTF-8"))
    url = response["url"]
    category = response["categorization"][0]["name"]
    lista.append(url)
    lista.append(category)
    listatotal.append(lista)
    print 'url: ' + url + '  -  Categoria: ' + category
