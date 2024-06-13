import numpy as np

impuestos = [0.16, 0.2, 0.06, 0.06, 0.07, 0.17, 0.06, 0.22]

cuartiles = np.quantile(impuestos, [0.25, 0.5, 0.75])

print(f"Cuartil 1: {cuartiles[0]} \nCuartil 2: {cuartiles[1]} \nCuartil 3: {cuartiles[2]}")


