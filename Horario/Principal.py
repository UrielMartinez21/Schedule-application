import Paquete.Menu as menu                 # Mensajes de menu
import Paquete.Inicio as inicio             # Funciones de arranque
import Paquete.Excel as excel               # Funciones menu 1
import Paquete.Horario as horario           # Funciones menu 2
import Paquete.Consultas as consultas       # Funciones menu 3
from os import *

inicio.Bienvenida()
nameArchivo = inicio.Ingresar_Archivo("TablaProfesores.xlsx")
tablaExcel = inicio.Importar_Excel(nameArchivo)

while True:
    menu.Menu_General()
    opcionMenu=int(input("Opcion: "))
    system("cls")

    if opcionMenu==1:
        print("[+]Crear archivo excel")
        menu.Menu_Excel()
        opcionExcel=int(input("Opcion: "))
        excel.Crear_Excel(opcionExcel, tablaExcel)

    elif opcionMenu==2:
        print("[+]Generar horario de clases")
        listaAprobada=horario.Materias_Aprobadas(tablaExcel)
        horario.Mostar_Materias(listaAprobada)

    elif opcionMenu==3:
        print("[+]Hacer consultas por dias de la semana")
        numeroDias=int(input("[+]Escoje cuantos dias quieres revisar: "))
        consultas.Consultar_Dias(tablaExcel,numeroDias)
    elif opcionMenu==4:
        print("[+]Saliendo del codigo...")
        break
