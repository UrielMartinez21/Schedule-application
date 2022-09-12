#------------------- Librerias -------------------

import os
import pandas as pd

#------------------- Funciones -------------------

# Ingresar el nombre del archivo excel
def Ingresar_Archivo(nombre_de_archivo):
    if os.path.isfile(nombre_de_archivo):
        archivo = nombre_de_archivo
        return archivo

# Importamos el archivo excel para su lectura
def Importar_Excel(archivo_excel):
    tabla = pd.read_excel(archivo_excel, sheet_name="Hoja1", header=0)
    return tabla

# Comprobamos que se haya creado el archivo
def Eliminar(nombre_de_archivo):
    if os.path.isfile(nombre_de_archivo):
        os.remove(nombre_de_archivo)
        print("[+]Se elimino el archivo")
    else:
        print("[+]No existe el archivo")

# Convertimos de Excel a CSV
def Excel_to_CSV(nombreExcel,nombreCSV,valor):
    if valor:
        Eliminar(nombreCSV)
        excel = Ingresar_Archivo(nombreExcel)
        tablaDatos=Importar_Excel(excel)
        tablaDatos.to_csv(nombreCSV, index=False)

# Interpreta el resultado
def clasificar(valor):
    if valor == 1:
        print("[+]El profesor es: estricto")
    elif valor == 2:
        print("[+]El profesor es: regular")
    elif valor == 3:
        print("[+]El profesor es: bueno")
    elif valor == 4:
        print("[+]El profesor es: barco")
    else:
        print("[+]Se desconoce al grupo que pertenece")

# Abrir archivo CSV
def Abrir_CSV(nombreCSV):
    with open(nombreCSV) as data:
        df = pd.read_csv(data)
    return df

