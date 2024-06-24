from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score

data = load_breast_cancer()

x = data.data
y = data.target

kfold = KFold(n_splits=3)

model = LogisticRegression(max_iter=10000)

scoring = "f1"
results = cross_val_score(model, x, y, cv=kfold, scoring=scoring)

print(f"Resultados de la prueba: {results}")
print(f"Resultado promedio de la prueba: {results.mean()}")