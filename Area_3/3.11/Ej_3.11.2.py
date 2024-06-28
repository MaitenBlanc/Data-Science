from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

diabetes = datasets.load_diabetes()

X = diabetes.data[:, :2]
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo de regresión lineal
reg = LinearRegression().fit(X_train, y_train)
y_pred = reg.predict(X_test)

print(f"Variables independientes: {reg.coef_}")
print(f"Variable dependiente: {reg.intercept_}")

# Crear figura
fig = plt.figure(figsize=(8, 6))

# Graficar puntos de entrenamiento, prueba y recta de regresión
plt.scatter(y_test, y_pred, color="blue")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="red")

plt.title("Recta de regresión múltiple")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()

