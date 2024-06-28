from sklearn import datasets
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

ridge = Ridge(alpha=0.1)

ridge.fit(X_test, y_test)

y_pred = ridge.predict(X_test)

# Cálculo de la puntuación del modelo
score = ridge.score(X_test, y_test)

# Mostrar resultados
print(f"Puntuación del modelo: {score}")
print(f"Coeficientes: \n{ridge.coef_}")
print(f"Término independiente: {ridge.intercept_}")