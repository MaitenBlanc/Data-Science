import numpy as np

route = "./archivos/apellidos_mas_frecuentes_pais_Argentina.csv"

data = np.genfromtxt(route, delimiter=",", encoding="utf-8", dtype=None, names=True)

for name in data.dtype.names:
    print(name.upper(), ":", data[name])