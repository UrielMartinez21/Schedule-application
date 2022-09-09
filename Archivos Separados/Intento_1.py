import pandas as pd             # Libreria de DataFrames
from pandas import ExcelWriter  # Importamos ExcelWriter
import openpyxl                 # Libreria de apoyo para excel
import os                       # Libreria que interactuara con el sistema

#.................Importar datos.................

# 1er arg= nombre del archivo   /   2do arg= hoja que se leera  /   3er arg= fila que sera encabezado
df = pd.read_excel("horario.xlsx", sheet_name="Hoja1", header=1)
#print(df)

#.................Filtrar Informacion.................

c=df[df["Asignatura"]=="COMPILADORES"]          #Guardo los profesores de compiladores
c2=c[["Grupo", "Asignatura", "Profesor"]]       #Filtro columnas de comp         
c3=c2.assign(Puntuacion="", Recomiendan="", Dificultad="", Observacion="", Orden="")
#print(c3)

rc=df[df["Asignatura"]=="REDES DE COMPUTADORAS"]        
rc2=rc[["Grupo", "Asignatura", "Profesor"]]         
rc3=rc2.assign(Puntuacion="", Recomiendan="", Dificultad="", Observacion="", Orden="")
#print(rc3)


#.................Exportar datos.................

# 1er arg = nombre del nuevo archivo
# 2do arg = elimino los indices
# 3er arg = Nombre de la hoja de excel

with ExcelWriter("materias.xlsx") as writer:
    c3.to_excel(writer, index=False, sheet_name="COMPILADORES")
    rc3.to_excel(writer, index=False, sheet_name="REDES")

#.................Verificacion de archivo creado.................

if os.path.isfile("materias.xlsx"):
    print("[+]Se creo el archivo")
else:
    print("[+]No se creo el archivo")