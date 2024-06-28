from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

diabetes = datasets.load_diabetes()

X = diabetes.data
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = LogisticRegression(max_iter=1000)

# Entrenamiento del modelo
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

# Evaluación del modelo
print(f"Precisión: {clf.score(X_test, y_test)*100}%")