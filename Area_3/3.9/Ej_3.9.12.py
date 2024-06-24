from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
x = iris.data
y = iris.target

model = DecisionTreeClassifier()

param_grid = {"max_depth":[4], "criterion":["entropy"]}

rsearch = GridSearchCV(estimator=model, param_grid=param_grid)
rsearch.fit(x,y)

print("Puntuación del modelo:", rsearch.score(x,y))
print("Mejor puntuación:", rsearch.best_score_)
print("Configuración:", rsearch.best_params_)