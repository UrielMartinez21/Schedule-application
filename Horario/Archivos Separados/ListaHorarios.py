#       ---> Genera horarios acorde a las entradas <---
#------------ Librerias ------------

import pandas as pd             # Libreria de DataFrames
from pandas import ExcelWriter  # Importamos ExcelWriter
import openpyxl                 # Libreria de apoyo para excel

#------------ Funciones ------------

def Bienvenida():
    print("[+]Ejecucion en proceso...\n")

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

# Se introducira las materias y grupos que se quieran meter
def Filtrar(df):
    lista=[]
    num=int(input("[+]Ingresa numero de materias: "))
    for x in range(num):
        materia=input(f"\t[+]Materia {x+1}:\t")
        grupo=input(f"\t[+]Grupo {x+1}:\t")
        filtrado=df[(df["Asignatura"]==materia) & (df["Grupo"]==grupo)]
        filtrado2=filtrado[["Grupo","Asignatura","Lun","Mar","Mie","Jue","Vie"]]         
        lista.append(filtrado2)
    return lista

# Filtrara que materias son incompatibles
def CompararMaterias(lista):
    print("[+]Materias incompatibles...")
    Dias=["Lun","Mar","Mie","Jue","Vie"]
    for x in range(len(lista)):                                 # Para materia 1
        for y in range(len(lista)):                             # Para materia 2
            for z in Dias:                                      # Para comparar dias
                if (y==x) or (x>y):                             # Se menor 'y' o igual a 'x' no se ejecutara  
                    continue
                else:
                    cp1 = lista[x][[z]].reset_index(drop=True)  # Variables para comparar
                    cp2 = lista[y][[z]].reset_index(drop=True)

                    show1 = lista[x][["Asignatura"]].to_numpy() # Variables para mostrar
                    show2 = lista[y][["Asignatura"]].to_numpy()
                        
                    if (cp1==cp2).bool():                       # Verifica que los dias no se traslapen
                        print(f"[-]Incompatibles:\t {show1}  y  {show2}")
                        break


#------------ Ejecucion de codigo ------------

Bienvenida()
archivo = Ingresar_Archivo("TablaProfesores.xlsx")
tabla=Importar_Excel(archivo)
# lista=Filtrar(tabla)

lista=[]
for x in range(3):
    materia=["COMPILADORES", "PROCESAMIENTO DIGITAL DE SEÑALES", "INSTRUMENTACION Y CONTROL"]
    grupo=["5CM1","5CM1","5CM2"]
    filtrado=tabla[(tabla["Asignatura"]==materia[x]) & (tabla["Grupo"]==grupo[x])]
    filtrado2=filtrado[["Grupo","Asignatura","Lun","Mar","Mie","Jue","Vie"]]         
    lista.append(filtrado2)


CompararMaterias(lista)

