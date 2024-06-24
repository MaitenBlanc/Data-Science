from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import LeaveOneOut, cross_val_score

iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target

loocv = LeaveOneOut()

model = LogisticRegression()

results = cross_val_score(model, X, y, cv=loocv)

print(results)