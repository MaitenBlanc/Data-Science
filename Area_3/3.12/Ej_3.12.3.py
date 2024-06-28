from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_gaussian_quantiles
from sklearn.metrics import silhouette_score

# Conjunto de datos
X, y_clusters = make_gaussian_quantiles(n_samples=150, random_state=42)

# Cálculo de coeficientes
coef_avgs= []

for i in range(2, 10):
    kmeans = KMeans(n_clusters=i, n_init=10).fit(X)
    coef_avgs.append(silhouette_score(X, kmeans.labels_, metric='euclidean'))

# Gráfica
plt.title("Método de Shilhouette")
plt.xlabel("Clústeres")
plt.ylabel("Coeficiente")
plt.grid()
plt.plot(range(2, 10), coef_avgs, 'bx-')
plt.show()