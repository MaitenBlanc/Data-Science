from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score

iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target

kfold = KFold(n_splits = 4)

model = LogisticRegression()

results = cross_val_score(model, X, y, cv=kfold)
print(f"Resultados de los 4 k-folds: \n{results}")