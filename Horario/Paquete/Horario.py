#---------------------- Librerias  ----------------------

# from Funciones import Bienvenida,Ingresar_Archivo,Importar_Excel

#---------------------- Funciones  ----------------------

def Ingresar_Materia(tabla_excel):
    # ENTRADAS DE TEXTO
    materiaClave=input("\t[+]Ingresa la clave de la materia: ")
    # BUSCARA LA MATERIA EN EL DATAFRAME
    buscarMateria=tabla_excel[tabla_excel["Clave"]==materiaClave]
    # FILTRARA LA MATERIA
    materiaFiltrada=buscarMateria[["Grupo","Asignatura","Lun","Mar","Mie","Jue","Vie"]]
    return materiaFiltrada


def Comparar(lista,materiaC):
    Dias = ["Lun", "Mar", "Mie", "Jue", "Vie"]
    contador=0
    puntos=5*len(lista)
    # COMPARA DIAS POR MATERIA
    for dia in Dias:
        for materia in range(len(lista)):
            cp1 = lista[materia][[dia]].reset_index(drop=True)
            cp2 = materiaC[[dia]].reset_index(drop=True)
            if (cp1 == cp2).bool():
                break
            else:
                contador+=1
    # print(f"El contador llego a : {contador}, no llego a: {puntos}")
    if contador==puntos:
        contador=0
        return True
    else:
        contador=0
        return False

def Materias_Aprobadas(tabla_excel):
    listaMaterias=[]

    materiasTotales = int(input("[+]Numero de materias: "))

    materiaL=Ingresar_Materia(tabla_excel)
    listaMaterias.append(materiaL)

    while len(listaMaterias) < materiasTotales:
        materia=Ingresar_Materia(tabla_excel)
        aprobado=Comparar(listaMaterias,materia)
        show = materia[["Asignatura"]].to_numpy()
        if aprobado:
            listaMaterias.append(materia)
            print(f"[+]Se agrego:\t{show}")
        else:
            print(f"[+]No se agrego:\t{show}")
    return listaMaterias


def Mostar_Materias(lista):
    for numero in lista:
        print(numero)

#---------------------- Ejecucion de codigo  ----------------------

# Bienvenida()
# nameArchivo = Ingresar_Archivo("TablaProfesores.xlsx")
# tablaExcel = Importar_Excel(nameArchivo)

# lista=Materias_Aprobadas(tablaExcel)
# print(f"La lista tiene: {len(lista)} elementos dentro")
# Mostar_Materias(lista)
