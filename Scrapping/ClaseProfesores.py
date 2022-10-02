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
        if self.url is not None:
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
            print(f"[+]Se creo el profesor: {self.nombreProf}")
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
        print("Se agregaron sus datos\n")
        return self.Diccionario

class Profesores:
    #---> Variables a usar
    lista=[]
    lineas=None

    def __init__(self,archivo=None):
        self.archivo=archivo
        if self.archivo is not None:
            #---> Registros que seran leidos
            with open (self.archivo,"r") as data:
                lineas_totales=sum(1 for line in data)
                self.lineas=lineas_totales                 
            print("[+]Profesores creados.\n")
        else:
            print("No hay archivo que leer")

    def Agregar_Profesores(self):
        with open(self.archivo,"r") as data:
            for x in range(self.lineas):
                link=data.readline()
                maestro=Profesor(link)
                # maestro.Mostrar_Datos()
                DatosProf=maestro.Crear_Diccionario()
                self.lista.append(DatosProf)
        print(f"\nProfesores agregados:{len(self.lista)}")

    def Ver_Registro(self):
        print(self.lista)

maestro=Profesores("Links.txt")
maestro.Agregar_Profesores()
maestro.Ver_Registro()



#------------- Pasarlo a un dataframe
#------------- Crear un csv con todos esos datos
