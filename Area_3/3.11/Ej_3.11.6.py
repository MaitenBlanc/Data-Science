from sklearn import datasets
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split

diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Objeto Lasso y entrenamiento
alpha = 0.5
reg = Lasso(alpha=alpha)
reg.fit(X_test, y_test)

# Puntuación del modelo
score = reg.score(X_test, y_test)

# Mostrar resultados
print(f"Coeficientes: \n{reg.coef_}\n")
print(f"Término independiente: {reg.intercept_}")
print(f"Puntuación del modelo: {score}")


