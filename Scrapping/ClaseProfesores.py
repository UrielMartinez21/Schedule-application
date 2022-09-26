#------------------| Uso de librerias |------------------
from bs4 import BeautifulSoup                   # Interactuar con documento HTML
import requests                                 # Obtener datos de internet

#------------------| Creacion de Clases |------------------
class Profesor:
    #---> Variables a usar
    nombreProf=None
    Calidad=None
    Recomiendan=None
    Dificultad=None
    Diccionario=None

    def __init__(self,url=None):
        self.url=url
        if (self.url is not None):
            #---> Obtener datos de sitio web
            resultado=requests.get(self.url)                    # Obtener datos de la pagina
            soup=BeautifulSoup(resultado.text,"html.parser")    # Pasar a formato Beautiful
            #---> Nombre de profesor
            nombre=soup.find("b").get_text()                    # Nombre del docente
            self.nombreProf=nombre.title()
            #---> Puntos de profesor
            calif = []
            datos = soup.find_all("div", class_="grade")        # Puntuacion del docente
            for x in datos:
                valor=x.get_text(strip=True,separator=' ')      # Obtener solo el dato     
                calif.append(valor)
            #---> Formateo de string
            characters = "%"
            calif[1] = ''.join(x for x in calif[1] if x not in characters)
            #---> Asignacion de valores
            self.Calidad=calif[0]
            self.Recomiendan=calif[1]
            self.Dificultad=calif[2]
            #---> Mensaje de finalizacion
            print("[+]Se creo el profesor...")
        else:
            print("[+]No hay url...\n")

    def Mostrar_Datos(self):
        print(f"Profesor: {self.nombreProf}")
        print(f"Calidad:\t{self.Calidad}\nRecomiendan:\t{self.Recomiendan}\nDificultad:\t{self.Dificultad}\n")

    def Crear_Diccionario(self):
        self.Diccionario={
            "nombre":self.nombreProf,
            "calidad":self.Calidad,
            "recomiendan":self.Recomiendan,
            "dificultad":self.Dificultad}
        print(f"Se agregaron datos de: {self.nombreProf}\n")
        return self.Diccionario

#------------- Meter todo esto en una clase nueva
#------------- Agregar todos los datos en un diccionario
#------------- Pasarlo a un dataframe
#------------- Crear un csv con todos esos datos

ListaProf=[]

with open('Links.txt') as myfile:
    total_lines = sum(1 for line in myfile)


with open("Links.txt","r") as data:
    # print(total_lines)
    for x in range(total_lines):
        link=data.readline()
        # print(link)
        Profesor_X=Profesor(link)
        # Profesor_X.Mostrar_Datos()
        DatosProf=Profesor_X.Crear_Diccionario()
        ListaProf.append(DatosProf)

print(f"\nProfesores agregados: {len(ListaProf)}")
