from matplotlib import pyplot as plt
from sklearn.datasets import make_gaussian_quantiles
from scipy.cluster.hierarchy import linkage, dendrogram

# Conjunto de datos
X, y = make_gaussian_quantiles(n_samples=150, random_state=42)

# Matriz de enlace para el agrupamiento jerárquico
Z = linkage(X, method='complete', metric='euclidean')

# Dendrograma
dendrogram(Z)
plt.grid()
plt.show()