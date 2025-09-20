# ------------------| Uso de librerias |------------------
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

def obtener_links():
    # ------------------| Obtener codigo HTML |------------------
    r = urlopen("https://www.misprofesores.com/escuelas/IPN-ESCOM_1694/")
    bs = BeautifulSoup(r.read(), "html.parser")
    r.close()

    # ------------------| Obtener script y convertirlo a texto |------------------
    parte_objetivo = bs.find_all("script")[10].get_text()

    # ------------------| Obtener dataset de la parte objetivo |------------------
    dataset = [texto[texto.index("=")+2:-1] for texto in parte_objetivo.split("\n") if texto.startswith("var dataSet")]
    lista_objetos = json.loads(dataset[0])      # Convertir string a lista de objetos


    # ------------------| Crear link de cada profesor |------------------
    for objeto in lista_objetos:
        # url base de consultar
        url = "https://www.misprofesores.com/profesores/"
        
        # combinacion de profesor
        apellidos = objeto["a"].replace(' ', '-')
        # print(f"{objeto['n']}-{apellidos}_{objeto['i']}")

        # url completa
        url_completa = url + f"{objeto['n']}-{apellidos}_{objeto['i']}\n"
        # print(url_completa)
        with open('Scrapping/links_profesores.txt', 'a') as archivo:
            archivo.write(f"{url_completa}")