#------------------| Uso de librerias |------------------
from bs4 import BeautifulSoup                   # Interactuar con documento HTML
import requests                                 # Obtener datos de internet
import pandas as pd                             # Guardar datos en DataFrame

#------------------| Extraer datos de pagina |------------------
url = "https://www.misprofesores.com/profesores/eduardo-alfaro-miranda_39427"

resultado=requests.get(url)                         # Obtener datos de la pagina
soup=BeautifulSoup(resultado.text,"html.parser")    # Pasar a formato Beautiful                        

#------------------| Filtrar elementos HTML |------------------
nombre=soup.find("b").get_text()                    # Nombre del docente
nombreProf=nombre.title()
print(nombreProf)

datos = soup.find_all("div", class_="grade")        # Puntuacion del docente
calif=[]
for x in datos:
    valor=x.get_text(strip=True,separator=' ')      # Obtener solo el dato     
    calif.append(valor)
# print(calif)

characters = "%"
calif[1] = ''.join(x for x in calif[1] if x not in characters)
print(calif)

#------------------| Creacion de Dataframe |------------------
# df=pd.DataFrame()
# df["Profesor","Puntuacion","Dificultad","Recomiendad"]=None
# print(df)