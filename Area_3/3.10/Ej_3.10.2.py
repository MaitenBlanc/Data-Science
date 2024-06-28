from collections import Counter
from matplotlib import pyplot as plt
from sklearn import datasets
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import NearMiss

iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7)

us = NearMiss(n_neighbors=3, version=2)
X_train_res, y_train_res = us.fit_resample(X_train, y_train)

# Balanceo de datos
def run_model(X_train, X_test, y_train, y_test):
    clf = LogisticRegression(C=1.0, penalty='l2', random_state=1, solver="newton-cg")
    clf.fit(X_train, y_train)
    return clf

def show_results(y_test, pred_y):
    conf_matrix = confusion_matrix(y_test, pred_y)
    plt.figure(figsize = (8, 8))
    sns.heatmap(conf_matrix, xticklabels=iris.target_names, yticklabels=iris.target_names, annot=True, fmt="d")
    plt.title("Matriz de confusión")
    plt.ylabel("True class")
    plt.xlabel("Predicted class")
    display = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=iris.target_names)
    display.plot()
    plt.show()
    print(classification_report(y_test, pred_y))

# Mostrar resultados
print(f"Distribución antes del balanceo: {Counter(y_train)}")
print(f"Distribución después del balanceo: {Counter(y_train_res)}")

# Entrenamiento y testing
model = run_model(X_train_res, X_test, y_train_res, y_test)

pred_y = model.predict(X_test)
show_results(y_test, pred_y)