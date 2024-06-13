import statistics
import numpy as np

notas = [5, 3, 6, 5, 4, 5, 7, 8, 6, 5, 6, 8, 3, 4, 5, 4, 8, 5, 5, 4]

# a) La media
print(f"Media: {statistics.mean(notas)}")

# b) La mediana
print(f"Mediana: {np.median(notas)}")

# c) Los cuartiles Q1, Q2 y Q3
Q1 = np.quantile(notas, 0.25)
Q3 = np.quantile(notas, 0.75)
print(f"Cuantil 1: {Q1} \nCuantil 2: {np.quantile(notas, 0.5)} \nCuantil 3: {Q3}")

# d) Los percentiles P30 y P80
print(f"Percentil 30: {np.percentile(notas, 30)} \nPercentil 80: {np.percentile(notas, 80)}")

# e) La desviación típica
print(f"Desviación típica: {np.std(notas)}")

# f) La varianza
print(f"Varianza: {np.var(notas)}")

# g) El rango intercuartílico
print(f"Rango intercuartílico: {Q3 - Q1}")