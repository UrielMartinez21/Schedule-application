#------------------- Librerias a usar -------------------
import Paquete.Funciones as fn                                      # Funciones de arranque
import Paquete.Predicciones as predicion

from sklearn.model_selection import train_test_split                # Area de entrenamiento y testing

#------------------- Pasos previos -------------------
# fn.Excel_to_CSV("datosProfesores.xlsx", "data.csv")
datos=fn.Abrir_CSV("data.csv")
# print(datos)

#------------------- Clasificacion de valores -------------------
arreglox = datos[datos.columns[2:-1]].to_numpy()                    # Caracteristicas de profesores
arregloy = datos[datos.columns[-1]].to_numpy()                      # Etiquetas de profesores

#------------------- Area de entrenamiento y testing -------------------
X_train, X_test, y_train, y_test = train_test_split(arreglox, arregloy)
# print(f"[+]Datos para entrenamiento: {X_train.shape}")            # Prof. y caract. para entrenar

#------------------- Area de predicciones -------------------

predicion.Predecir(X_train, X_test, y_train, y_test,7)