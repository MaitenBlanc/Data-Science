from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

data = load_breast_cancer()

x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=10000)

model.fit(x_train, y_train)

predicted = model.predict(x_test)
matrix = confusion_matrix(y_test, predicted)

# Gráfico de la matriz de confusión
display = metrics.ConfusionMatrixDisplay(confusion_matrix = matrix, display_labels = data.target_names)
display.plot()
plt.title("Matriz de confusión")
plt.show()

print(f"Matriz de confusión: \n{display}")