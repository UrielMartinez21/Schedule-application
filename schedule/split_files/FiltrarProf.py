#       ---> Organiza a los profesores por materia <---
#------------ Librerias ------------

import pandas as pd             # Libreria de DataFrames
from pandas import ExcelWriter  # Importamos ExcelWriter
import openpyxl                 # Libreria de apoyo para excel
import os                       # Libreria que interactuara con el sistema

#------------ Funciones ------------

# Ingresar el nombre del archivo excel
def Ingresar_Archivo(texto):
    archivo=texto
    # archivo = input("[+]Ingresar el nombre del archivo: ") + ".xlsx"
    # archivo="TablaProfesores.xlsx"
    return archivo

# Importamos el archivo excel para su lectura
def Importar_Excel(archivo):
    df = pd.read_excel(archivo, sheet_name="Hoja1", header=1)
    return df

# Nombre de todas las materias
def ListaDeMaterias():
    lista_materias=[]
    cantidad=int(input("[+]Total de materias: "))
    for x in range(0,cantidad):
        materias=input(f"\t[+]Materia {x}: ")
        lista_materias.append(materias)
    return lista_materias

# Nombre de pestañas de Excel
def ListaDePestanas(lista_de_materias):
    lista_pestanas=[]
    print(f"[+]Total de pestanas: {len(lista_de_materias)}")
    for x in range(0,len(lista_de_materias)):
        pestanas=input(f"\t[+]Pestana {x}: ")
        lista_pestanas.append(pestanas)
    return lista_pestanas

# Clasificamos los por materias
def Filtrar(df,lista_materias):
    listaDF=[]
    for x in range(0,len(lista_materias)):
        materia1=df[df["Asignatura"]==lista_materias[x]]
        materia2=materia1[["Grupo", "Asignatura", "Profesor"]]         
        materia3=materia2.assign(Puntuacion="", Recomiendan="", Dificultad="", Observacion="", Orden="")
        listaDF.append(materia3)
    return listaDF

# Convertimos los datos filtrados a un archivio excel
def Exportar_Excel(lista_filtrada,lista_nombres):
    with ExcelWriter("materias.xlsx") as writer:
        for var in range(0,len(lista_filtrada)):
            lista_filtrada[var].to_excel(writer, index=False, sheet_name=lista_nombres[var])

# Comprobamos que se haya creado el archivo
def Verificar():
    # archivo = input("[+]Verificar archivo: ") + ".xlsx"
    archivo="materias.xlsx"
    if os.path.isfile(archivo):
        print("[+]El archivo existe")
    else:
        print("[+]El archivo no existe")

#------------ Ejecucion de codigo ------------

nombre_de_archivo=Ingresar_Archivo("TablaProfesores.xlsx")
tabla_de_datos=Importar_Excel(nombre_de_archivo)

nombre_de_materias=ListaDeMaterias()
lista_filtrada=Filtrar(tabla_de_datos,nombre_de_materias)

pestanas=ListaDePestanas(nombre_de_materias)

Exportar_Excel(lista_filtrada,pestanas)
Verificar()