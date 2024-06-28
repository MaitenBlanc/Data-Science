import numpy as np
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB

digits = datasets.load_digits()
X = digits.data
y = digits.target

clf = MultinomialNB()

clf.fit(X, y)

test_data = np.random.rand(1, X.shape[1])

predicciones = clf.predict(X)

print(f"Predicciones: {predicciones}")
print(f"Exactitud: {accuracy_score(y, predicciones)}")