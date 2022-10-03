#------------------| Uso de librerias |------------------
from bs4 import BeautifulSoup                   # Interactuar con documento HTML
import requests                                 # Obtener datos de internet
import pandas as pd                             # Crear un solo registro de datos

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

    def Valores(self):
        # print("Se agregaron sus datos\n")
        return (self.nombreProf,self.Calidad,self.Recomiendan,self.Dificultad)

class Profesores:
    #---> Variables a usar
    listaNombres=[]
    listaCalidad=[]
    listaRecomiendan=[]
    listaDificultad=[]

    lineas=None

    tabla=None

    def __init__(self,archivo=None):
        self.archivo=archivo
        if self.archivo is not None:
            #---> Registros que seran leidos
            with open (self.archivo,"r") as data:
                lineas_totales=sum(1 for line in data)  # Numeros totales de links
                self.lineas=lineas_totales              # Asignar valor a variable
            print("[+]Profesores creados...\n")
        else:
            print("No hay archivo que leer")

    def Agregar_Profesores(self):
        with open(self.archivo,"r") as data:            # Se abre el archivo de links
            for x in range(self.lineas):
                link=data.readline()                    # Se guarda el link 
                maestro=Profesor(link)                  # Se pasa a link a clase Profesor
                #---> Separacion de datos
                nombre, calidad, recomiendan, dificultad = maestro.Valores()
                #---> Llenado de listas
                self.listaNombres.append(nombre)
                self.listaCalidad.append(calidad)
                self.listaRecomiendan.append(recomiendan)
                self.listaDificultad.append(dificultad)
        print(f"\nProfesores agregados:{len(self.listaNombres)}\n")

    def Ver_Profesores(self):
        print(self.listaNombres)
        print(self.listaCalidad)
        print(self.listaRecomiendan)
        print(self.listaDificultad)

    def Tabla(self):
        df=pd.DataFrame(columns=["Nombre","Calidad","Recomiendan","Dificultad"])
        df["Nombre"]=self.listaNombres
        df["Calidad"]=self.listaCalidad
        df["Recomiendan"]=self.listaRecomiendan
        df["Dificultad"]=self.listaDificultad
        self.tabla=df
        print(self.tabla)

    def Exportar_Tabla(self):
        self.tabla.to_csv("Datos.csv",index=False)
        print("Se exportaron los datos")
