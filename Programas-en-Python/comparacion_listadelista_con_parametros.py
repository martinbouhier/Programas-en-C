
a = [['1', 'A', 'a', '300'],
     ['1', 'B', 'b', '30'],
     ['1', 'C', 'c', '100'],
     ['1', 'D', 'd', '4500'],
     ['2', 'A', 'a', '3'],
     ['2', 'B', 'b', '302'],
     ['2', 'X', 'x', '98'],
     ['2', 'Z', 'z', '276'],
     ['3', 'A', 'a', '54'],
     ['3', 'B', 'b', '65'],
     ['3', 'F', 'f', '76'],
     ['3', 'Y', 'y', '99']]


este_mes = []
resto = []
changes = []
for item in a:
    if item[0] == '1':
        este_mes.append(item)
    else:
        resto.append(item)


for item in este_mes:
    for rest in resto:
        if (item[1] == rest[1] and item[2] == rest[2]):
            rest = [rest[0]] + [item[1]] + [item[2]] + ([float(item[3]) - float(rest[3])])
            changes.append(rest)
            resto.remove(rest)
