import Paquete.Funciones as fn 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

datos = fn.Abrir_CSV("data.csv")
dataFrame= pd.DataFrame(datos)
# print(dataFrame)

dataFrame.groupby("Etiqueta")["Puntuacion"].sum().plot(kind="bar")
plt.title("Grafica")
plt.xlabel("Etiqueta")
plt.ylabel("Puntuacion")
plt.show()