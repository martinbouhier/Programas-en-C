# encoding=utf8
# -*- coding: utf-8 -*-
import csv
import pandas as pd
from pathlib import Path
from csv import reader as csvreader
import os
import sys
import signal


nuevo = []
file = "database.csv"

print '1 - Cargar'
print '2 - Buscar'
print '3 - Editar'
print '4 - Salir'
accion = raw_input()
if accion == '4':
    os.kill(os.getppid(), signal.SIGHUP)
else:
    pass

my_file = Path(file)
if my_file.is_file():
    with open(file, 'r') as fp:
        reader = csvreader(fp)
        li = list(reader)

    if accion == '1':
        print 'Cliente:'
        cliente = raw_input()
        print 'Fecha:'
        fecha = raw_input()
        print 'Informe:'
        informe = raw_input()

        nuevo.append(cliente)
        nuevo.append(fecha)
        nuevo.append(informe)
        li.append(nuevo)

        with open(file, "wb") as f:
            writer = csv.writer(f)
            writer.writerows(li)
        os.system('cls' if os.name == 'nt' else 'clear')
        os.execl(sys.executable, sys.executable, * sys.argv)

    if accion == '2':
        df = pd.read_csv(file)
        print '1 - Cliente'
        print '2 - Fecha'
        print '3 - Editar'
        print '4 - Salir'
        buscar = raw_input()
        opcion = raw_input()
        if buscar == '4':
            os.kill(os.getppid(), signal.SIGHUP)
        if buscar == '1':
            df = df[(df['Cliente'] == opcion)]
            print df
        if buscar == '2':
            df = df[(df['Fecha'] == opcion)]
            print df
        if buscar == '3':
            df = df[(df['Editar'] == opcion)]
            print df
        os.system('cls' if os.name == 'nt' else 'clear')
        os.execl(sys.executable, sys.executable, * sys.argv)

else:
    database = [['Cliente', 'Fecha', 'Informe']]
    if accion == '1':
        print 'Cliente:'
        cliente = raw_input()
        print 'Fecha:'
        fecha = raw_input()
        print 'Informe:'
        informe = raw_input()
        nuevo.append(cliente)
        nuevo.append(fecha)
        nuevo.append(informe)
        database.append(nuevo)
        with open(file, "wb") as f:
            writer = csv.writer(f)
            writer.writerows(database)
    else:
        print 'No hay base de datos'
    os.system('cls' if os.name == 'nt' else 'clear')
    os.execl(sys.executable, sys.executable, *sys.argv)
