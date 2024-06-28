import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

digits = datasets.load_digits()
X = digits.data
y = digits.target

# Instancia del Random Forest con profundidad máxima de 5 y 10 árboles
clf = RandomForestClassifier(n_estimators=10, max_depth=4)

# Entrenamiento del modelo
clf = clf.fit(X, y)

random = np.random.rand(1, X.shape[1])
# Mostrar resultados
print(f"Puntuación: {clf.score(X, y)}")
print(f"Predicción de un elemento: {clf.predict(random)}")