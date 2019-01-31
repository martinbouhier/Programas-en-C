#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Primero que nada debemos tener creada la app necesaria que nos dará el .json
con los valores correspondientes para poder loguearnos en google
	Algo muy importante es que se deben habilitar dentro de las credenciales
de la app creada tanto el api de google_sheets como el de google_drive.
	El json deberá ser extraido desde la app y tedrá los siguientes campos:
	{
	  "type": "service_account",
	  "project_id": "drive-230113",
	  "private_key_id": "",
	  "private_key": "",
	  "client_email": "",
	  "client_id": "",
	  "auth_uri": "",
	  "token_uri": "",
	  "auth_provider_x509_cert_url": "",
	  "client_x509_cert_url": ""
	}
    Además debemos crear el documeto de excel_sheet en google,
compartirlo con el mail que veremos en "client_email": "" (dentro del json)
"""
import pandas as pd  # pandas 0.23.4
import pygsheets  # pygsheets 2.0.0

class Google:
    def __init__(self, service_file):
        self.service_file = service_file
    def update_sheet(self, file_name, csv_name, sheet, clean_start_cel, clean_end_cel, df_fila, df_columna):
        gc = pygsheets.authorize(service_file=self.service_file)
        sh = gc.open(file_name)
        wks = sh[sheet]
        wks.clear(start=clean_start_cel, end=clean_end_cel)
        df = pd.read_csv(csv_name)
        wks.set_dataframe(df,(df_fila, df_columna))


# Ingreso de valores para la clase y la función
##############################################################################################################
google = Google(\
    'google_sheets.json'  # Nombre del json donde se encuentran todos los valores necesarios para logearse en el api de google
)

google.update_sheet(\
    'Tracker_DBM',  # Nombre de archivo que se encuentra en google
    'tracker.csv',  # Nombre del CSV a cargar
    0,              # Numero de hoja dentro del archivo de google
    'A1',           # Celda de inicio a limpiar la hoja del archivo de google
    None,           # Celda de fin a limpiar la hoja del archivo de google
    1,              # Fila desde donde se van a introducir los datos del csv en el archivo de google
    1               # Columna desde donde se van a introducir los datos del csv en el archivo de google
)

##############################################################################################################
