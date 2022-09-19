# Ver que tan seguro se siente el algoritmo a la hora de clasificar un nuevo punto

#------------------- Librerias a usar -------------------
import Paquete.Funciones as fn                                  # Funciones de arranque

from sklearn.model_selection import train_test_split            # Area de entrenamiento y testing
from sklearn import svm                                         # Para usar estimadores de incertidumbre

#------------------- Cargar archivos -------------------
fn.Excel_to_CSV("datosProfesores.xlsx", "data.csv", False)
datos=fn.Abrir_CSV("data.csv")

#------------------- Preparar Aprendizaje -------------------
#---- Clasificacion de valores
arreglox = datos[datos.columns[2:-1]].to_numpy()                # Caracteristicas de profesores
arregloy = datos[datos.columns[-1]].to_numpy()                  # Etiquetas de profesores

#---- Area de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(arreglox, arregloy)

#------------------- EStimadores de Incertidumbre -------------------
algoritmo=svm.SVC(probability=True)
algoritmo.fit(X_train,y_train)

algoritmo.decision_function_shape="ovr"

# prueba=algoritmo.decision_function(X_test)[:4]
# print(prueba)

porcentaje=algoritmo.predict_proba(X_test)[:4]
print(porcentaje)