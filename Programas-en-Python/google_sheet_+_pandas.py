import pandas as pd
import pygsheets

class Google:
    def __init__(self, service_file):
        self.service_file = service_file
    def update_sheet(self, file_name, csv_name, sheet, clean_start_cel, clean_end_cel, df_fila, df_columna):
        gc = pygsheets.authorize(service_file=self.service_file)
        sh = gc.open(self.file_name)
        wks = sh[self.sheet]
        wks.clear(start=self.clean_start_cel, end=self.clean_end_cel)
        df = pd.read_csv(self.csv_name)
        wks.set_dataframe(df,(self.df_fila, self.df_columna))


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
