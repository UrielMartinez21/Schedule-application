#------------------> Uso de librerias <------------------
from bs4 import BeautifulSoup               # Interactuar con documento HTML
import requests                             # Obtener datos de internet
import pandas as pd                         # Guardar datos en DataFrame

#------------------> Clon de pagina <------------------
url = "https://www.misprofesores.com/profesores/Fanny-Adan-Sosa_135983"
pagina=requests.get(url)
soup=BeautifulSoup(pagina.content,"html.parser")


#------------------> Filtracion de elementos HTML <------------------
#----> Valoracion de profesor
opinion=soup.find_all("span", class_="rating-type")
evaluacion=[]
for x in opinion:
    evaluacion.append(x.text)
print(evaluacion)