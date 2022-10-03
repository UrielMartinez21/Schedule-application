#------------------| Uso de librerias |------------------
from bs4 import BeautifulSoup                   # Interactuar con documento HTML
import requests                                 # Obtener datos de internet

#------------------| Extraer datos de pagina |------------------
url = "https://www.misprofesores.com/profesores/eduardo-alfaro-miranda_39427"

resultado=requests.get(url)                         # Obtener datos de la pagina
soup=BeautifulSoup(resultado.text,"html.parser")    # Pasar a formato Beautiful                        

#------------------| Filtrar elementos HTML |------------------
nombre=soup.find("b").get_text()                    # Nombre del docente
print(nombre)