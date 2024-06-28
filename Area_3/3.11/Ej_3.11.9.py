import numpy as np
from sklearn import datasets, tree

digits = datasets.load_digits()
X = digits.data
y = digits.target

# Instancia del árbol de decisión con profundidad 8
clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=7)

# Entrenamiento del árbol
clf = clf.fit(X, y)

random = np.random.rand(1, X.shape[1])
# Mostrar resultados
print(f"Puntuación: {clf.score(X, y)}")
print(f"Predicción de un elemento: {clf.predict(random)}")