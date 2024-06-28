from matplotlib import pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression

diabetes = datasets.load_diabetes()
X_train = diabetes.data[:, np.newaxis, 0]
y_train = diabetes.target

# Modelo de regresión lineal
reg = LinearRegression().fit(X_train, y_train)

print(f"Coeficiente dependiente: {reg.coef_}")
print(f"Término independiente: {reg.intercept_}")

# Mostrar datos de entrenamiento
plt.scatter(X_train, y_train, color="blue")

# Mostrar línea de regresión
plt.plot(X_train, reg.predict(X_train), color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()