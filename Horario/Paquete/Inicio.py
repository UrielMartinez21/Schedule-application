#---------------------- Librerias ----------------------

import os                       # Libreria que interactuara con el sistema
import pandas as pd             # Libreria de DataFrames

#---------------------- Funciones de inicio ----------------------

# Mensaje de inicio de proceso
def Bienvenida():
    print("[+]Ejecucion en proceso...")

# Ingresar el nombre del archivo excel
def Ingresar_Archivo(nombre_de_archivo):
    if os.path.isfile(nombre_de_archivo):
        archivo = nombre_de_archivo
        return archivo

# Importamos el archivo excel para su lectura
def Importar_Excel(archivo_excel):
    tabla = pd.read_excel(archivo_excel, sheet_name="Hoja1", header=1)
    return tabla