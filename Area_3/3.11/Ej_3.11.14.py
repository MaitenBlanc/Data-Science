import numpy as np
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

digits = datasets.load_digits()
X = digits.data
y = digits.target

# Creación y entenamiento del modelo
clf = SVC()
clf.fit(X, y)

# Precisión del entrenamietno
y_pred = clf.predict(X)

precision = accuracy_score(y, y_pred)

random = np.random.rand(1, X.shape[1])

print(f"Exactitud: {precision}\n")
print(f"Predicción de una entrada: {clf.predict(random)}\n")
print(f"Vectores soporte: {clf.support_vectors_}")