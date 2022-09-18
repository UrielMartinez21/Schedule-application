# Aprendizaje supervisado con algoritmo clasificador
#------------------- Librerias a usar -------------------
import Paquete.Funciones as fn                                  # Funciones de arranque

from sklearn.model_selection import train_test_split            # Area de entrenamiento y testing
from sklearn.neighbors import KNeighborsClassifier              # Clasificador de vecinos cercanos

#------------------- Cargar archivos -------------------
fn.Excel_to_CSV("datosProfesores.xlsx", "data.csv", False)
datos=fn.Abrir_CSV("data.csv")
# print(datos)

#------------------- Preparar Aprendizaje -------------------
#---- Clasificacion de valores
arreglox = datos[datos.columns[2:-1]].to_numpy()                # Caracteristicas de profesores
arregloy = datos[datos.columns[-1]].to_numpy()                  # Etiquetas de profesores

#---- Area de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(arreglox, arregloy)
# print(f"[+]Datos para entrenamiento: {X_train.shape}")        # Prof. y caract. para entrenar

#------------------- Area de predicciones -------------------
Knn=KNeighborsClassifier(n_neighbors=5)                         # Considerar a los 7 vecinos mas cercanos
Knn.fit(X_train,y_train)                                        # Comando para entrenar
porcentaje=100*Knn.score(X_test, y_test)                        # Que tan bien aprendio

print("[+]Aprendizaje: {:.2f}%".format(porcentaje))              

#----  Prediccion
datos=[7,0.57,3.3]
fn.clasificar(Knn.predict([datos]))

