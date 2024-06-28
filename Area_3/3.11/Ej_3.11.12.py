import numpy as np
from sklearn import datasets
from xgboost import XGBClassifier
from sklearn.metrics import r2_score

digits = datasets.load_digits()
X = digits.data
y = digits.target

# Instancia del Random Forest con profundidad máxima de 5 y 10 árboles
model_xgb = XGBClassifier(n_estimator=10, max_depth=4)

# Entrenamiento del modelo
model_xgb.fit(X, y)

# Conjunto de entrenamiento
pred_xgb = model_xgb.predict(X)

# Puntuación del modelo
score = r2_score(y, pred_xgb)

random = np.random.rand(1, X.shape[1])
# Mostrar resultados
print(f"Puntuación: {score}")
print(f"Predicción de un elemento: {model_xgb.predict(random)}")