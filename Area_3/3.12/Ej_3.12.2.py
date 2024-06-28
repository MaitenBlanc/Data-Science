from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_gaussian_quantiles

# Conjunto de datos
X, y_clusters = make_gaussian_quantiles(n_samples=150, random_state=42)

distorsion = []

for i in range(1, 10):
    kmeans = KMeans(n_clusters=i, n_init=10).fit(X)
    distorsion.append(kmeans.inertia_)
    
# Gráfica
plt.title("Método de la dispersión")
plt.xlabel("Clústeres")
plt.ylabel("Distorsión")
plt.grid()
plt.plot(range(1,10), distorsion, 'bx-')
plt.show()