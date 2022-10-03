#------------------| Uso de librerias |------------------
import Paquetes.Clases as cp

#------------------| Ejecucion de codigo |------------------
datos=cp.Profesores("Links.txt")
datos.Agregar_Profesores()
datos.Tabla()
# datos.Exportar_Tabla()