#------------------- Librerias a usar -------------------
from sklearn.neighbors import KNeighborsClassifier          # Clasificador de vecinos cercanos
import Paquete.Funciones as fn

#------------------- Funciones a usar -------------------
def Predecir(X_train, X_test, y_train, y_test,valor):
    Knn=KNeighborsClassifier(n_neighbors=valor)                         # Considerar a los 7 vecinos mas cercanos
    Knn.fit(X_train,y_train)                                            # Comando para entrenar 'fit'
    print(f"[+]Porcentaje para predecir: {100*Knn.score(X_test, y_test)}")  # Que tan bien aprendio el algoritmo 
    #------------------- Prediccion -------------------
    fn.clasificar(Knn.predict([[6, 0.67, 5]]))                          # Puntuacion, Recomiendan, Dificultad