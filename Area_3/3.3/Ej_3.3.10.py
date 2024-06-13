from matplotlib import pyplot as plt
import numpy as np

edades = [25, 36, 25, 20, 35, 24, 42, 44, 51, 32, 36, 36, 25, 29,
        28, 25, 36, 37, 29, 44, 42, 41, 40, 40, 42, 51, 25, 26,
        28, 27, 32, 31, 30, 31, 39, 36, 36, 32, 23, 26, 24, 27, 46, 46, 48]

# Al máximo de edades se le suma 10 para que en el intervalo entren las edades mayores a 50
bins = range(min(edades), max(edades) + 10, 10)

plt.hist(edades, bins=bins, edgecolor="black")
plt.title("Histograma de edades")
plt.show()