#!/usr/bin/python
"""
Script para comprar items de dos listas distintas donde identificamos el item[0] (primer valor)
de cada lista de listas y si coinciden juntamos la información de ambas listas.
La respuesta será impresa en la consola y devuelta en un CSV.
"""


import csv

lista1 = [['Nombre', 'Nota'], ['Pedro', '10'], ['Jorge', '7'], ['David', '3'], ['Luis', '9']]
lista2 = [['Nombre', 'Profesión'], ['Pedro', 'Estudiante'], ['Jorge', 'Bailarin']]
lista = [['Nombre', 'Profesión', 'Nota']]

for item1 in lista1[1:]:
    for item2 in lista2[1:]:
        if item2[0] == item1[0]:
            item2.append(item1[0])
            lista.append(item2)

print lista

with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(lista)
