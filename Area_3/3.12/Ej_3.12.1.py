from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_gaussian_quantiles

# Conjunto de datos
X, y_clusters = make_gaussian_quantiles(n_samples=150, random_state=42)

kmeans = KMeans(n_clusters=3, random_state=0)

# Entrenamiento del modelo
kmeans.fit(X)

# Asignación de clúster y centroides
labels = kmeans.predict(X)

centroides = kmeans.cluster_centers_

print(f"Centroides: \n{centroides}")

# Visualización de datos y centroides
plt.scatter (X[:, 0], X[:, 1], c=labels)
plt.scatter(centroides[:, 0], centroides[:, 1], marker='x', s=200, linewidths=3, color='r')
plt.show()