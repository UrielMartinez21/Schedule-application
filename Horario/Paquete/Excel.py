#---------------------- Librerias ----------------------

from pandas import ExcelWriter  # Importamos ExcelWriter
import openpyxl                 # Libreria de apoyo para excel
import os                       # Libreria que interactuara con el sistema

#---------------------- Sub-funciones ----------------------

# Materias a incluir 
def Lista_De_Materias():
    lista_materias=[]
    cantidad=int(input("[+]Total de materias: "))
    for x in range(0,cantidad):
        materias=input(f"\t[+]Materia {x+1}: ")
        lista_materias.append(materias)
    return lista_materias

# Nombre de pestañas de Excel
def Lista_De_Pestanas(lista_de_materias):
    lista_pestanas=[]
    print(f"[+]Total de pestanas: {len(lista_de_materias)}")
    for x in range(0,len(lista_de_materias)):
        pestanas=input(f"\t[+]Pestana {x+1}: ")
        lista_pestanas.append(pestanas)
    return lista_pestanas

# Agregamos nuevas columnas a las materias
def Filtrar_Para_Excel(tabla_excel,lista_materias):
    listaDF=[]
    for x in range(0,len(lista_materias)):
        materia1 = tabla_excel[tabla_excel["Asignatura"]==lista_materias[x]]
        materia2 = materia1[["Grupo", "Asignatura", "Profesor"]]         
        materia3 = materia2.assign(Puntuacion = "", Recomiendan = "", Dificultad = "", Observacion = "", Orden = "")
        listaDF.append(materia3)
    return listaDF

def Exportar_Excel(lista_materias,lista_pestanas):

    """Exporta los datos a un archivo excel"""

    with ExcelWriter("Materias.xlsx") as writer:
        for var in range(0,len(lista_materias)):
            lista_materias[var].to_excel(writer, index=False, sheet_name=lista_pestanas[var])

def Verificar(nombre_de_archivo):

    """Verifica si se creo el archivo"""

    if os.path.isfile(nombre_de_archivo):
        print("[+]Se creo el archivo")
    else:
        print("[+]No se creo el archivo")

def all_Materias(tabla_excel):

    """Elimina las materias repetidas"""

    materias = list(tabla_excel.iloc[:, 2])
    newMaterias=[]
    for materia in materias:
        if materia not in newMaterias:
            newMaterias.append(materia)
    return newMaterias

# Agrega pestañas conforme la lista que le pasen
def all_Pestanas(Lista_materias):
    newLista = [pestana[0:30] for pestana in Lista_materias]
    return newLista

#---------------------- Funcion para exportar ----------------------

def Crear_Excel(opcion,tabla_de_excel):
    if opcion == 1:
        nameMaterias = Lista_De_Materias()
        pestanas = Lista_De_Pestanas(nameMaterias)

    elif opcion==2:
        nameMaterias = all_Materias(tabla_de_excel)
        pestanas = all_Pestanas(nameMaterias)

    lista_filtrada = Filtrar_Para_Excel(tabla_de_excel, nameMaterias)
    Exportar_Excel(lista_filtrada, pestanas)
    Verificar("Materias.xlsx")
    print(f"[+]Materias agregadas: {len(nameMaterias)}")
    print("Nombre de las materias agregadas: ")
    for materia in nameMaterias:
        print("\t[+]",materia)
