import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

digits = datasets.load_digits()
X = digits.data
y = digits.target

# Instancia del Random Forest con profundidad máxima de 10 y 50 árboles
clf = RandomForestClassifier(n_estimators=50, max_depth=9)

# Entrenamiento del modelo
clf = clf.fit(X, y)

random = np.random.rand(1, X.shape[1])
# Mostrar resultados
print(f"Puntuación: {clf.score(X, y)}")
print(f"Predicción de un elemento: {clf.predict(random)}")