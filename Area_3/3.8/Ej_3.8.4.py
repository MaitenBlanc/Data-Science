from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import ShuffleSplit, cross_val_score

iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target

kfold = ShuffleSplit(n_splits=4, test_size=0.2, random_state=2)

model = LogisticRegression()

results = cross_val_score(model, X, y, cv=kfold)

print(results)