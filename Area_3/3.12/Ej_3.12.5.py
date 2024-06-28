from matplotlib import pyplot as plt
from sklearn.datasets import make_gaussian_quantiles
from sklearn.cluster import DBSCAN

# Conjunto de datos
X, y_clusters = make_gaussian_quantiles(n_samples=150, random_state=42)

# Instancia DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=4)

# Entrenamiento del modelo
y_pred = dbscan.fit_predict(X)

# Número de clústers
if -1 in y_pred:
    n_clusters = len(set(y_pred)) - 1
else: 
    n_clusters = len(set(y_pred))

# Mostrar número de clústers
print(f"Clústers: {n_clusters}")

# Gráfica
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.grid()
plt.show()