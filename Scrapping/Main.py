#------------------| Uso de librerias |------------------
import Paquetes.Clases as cp
from Paquetes.funciones import obtener_links

#------------------| Ejecucion de codigo |------------------
# obtener_links()

datos=cp.Profesores("Scrapping/links_profesores.txt")
datos.Agregar_Profesores()
datos.Tabla()
datos.Exportar_Tabla()