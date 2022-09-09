#       ---> Hacer consultas de profesores <---
#------------ Librerias ------------

import pandas as pd             # Libreria de DataFrames
from pandas import ExcelWriter  # Importamos ExcelWriter
import openpyxl                 # Libreria de apoyo para excel

#------------ Funciones ------------

def Bienvenida():
    print("[+]Ejecucion en proceso...\n")

# Ingresar el nombre del archivo excel
def Ingresar_Archivo():
    # archivo = input("[+]Ingresar el nombre del archivo: ") + ".xlsx"
    archivo="TablaProfesores.xlsx"
    return archivo

# Importamos el archivo excel para su lectura
def Importar_Excel(archivo):
    df = pd.read_excel(archivo, sheet_name="Hoja1", header=1)
    return df

#------------ Ejecucion de codigo ------------
Bienvenida()
Archivo=Ingresar_Archivo()
df=Importar_Excel(Archivo)

resultado1= df[(df["Mar"] == "07:00-08:30") & (df["Mie"] == "07:00-08:30") & (df["Vie"] == "07:00-08:30")]
print(resultado1[["Grupo","Asignatura","Profesor","Lun","Mar","Mie","Jue","Vie"]])

# resultado2=df[(df["Lun"] == "08:30-10:00") & (df["Mie"] == "08:30-10:00") & (df["Jue"] == "08:30-10:00")]
# print(resultado2)
