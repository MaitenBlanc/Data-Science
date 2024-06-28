from matplotlib import pyplot as plt
from sklearn import datasets
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from imblearn.ensemble import BalancedBaggingClassifier
from sklearn.tree import DecisionTreeClassifier

iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7)

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

bbc = BalancedBaggingClassifier(estimator=DecisionTreeClassifier(), sampling_strategy='auto', replacement=False, random_state=0)

# Entrenamiento y testing
bbc.fit(X_train, y_train)
pred_y = bbc.predict(X_test)
show_results(y_test, pred_y)


