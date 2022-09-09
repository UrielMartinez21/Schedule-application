#------------- Area de importacion de librerias -------------
import Paquete.Funciones as fn                          # Funciones de arranque
import Paquete.Predicciones as predicion

from sklearn.model_selection import train_test_split    # Dividimos nuestro set en testing y entrenamiento
from sklearn.neural_network import MLPClassifier        # Clasificador de redes neuronales

#---------------- Preparacion ----------------
datos = fn.Abrir_CSV("data.csv")

arreglox = datos[datos.columns[2:-1]].to_numpy()        # Caracteristicas de profesores
arregloy = datos[datos.columns[-1]].to_numpy()          # Etiquetas de profesores

#---------------- Area de entrenamiento y testing ----------------
X_train,X_test,y_train,y_test=train_test_split(arreglox,arregloy)

# max_iter           = proceso donde se mandan informacion ocurrira 10 veces
# hidden_layer_sizes; 10 capaz y cada capa tendra 5 nodos
# Mientras menor sea el numero de iteraciones menor sera el numero de predicciones correctas

red = MLPClassifier(max_iter=10000, hidden_layer_sizes=(10,20))

red.fit(X_train,y_train)                                            # Variables de entrenamiento
print(f"[+]Porcentaje de acierto: {100*red.score(X_test,y_test)}")  # Porcentaje de predicciones que tuvo
predicion.Predecir(X_train, X_test, y_train, y_test, 7)
