#!/usr/bin/python
import csv

str1 = [['ID', 'URL', 'Volumen'], ['294041','bestjobs.co.za1','1427540'], ['294041','clarin.com','1427539']]
str2 = ['bestjobs.co.za', 'clarin.com', 'bingos.com.br']
nueva = [['ID', 'URL', 'Volumen']]

for item2 in str2:
    for item in str1:
        if item2 in item[1]:
            nueva.append(item)

# El script imprime las listas de str1 que estan en str2
print nueva

with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(nueva)


