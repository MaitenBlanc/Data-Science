import numpy as np

route = "./archivos/puntos_de_acceso_wifi_Mexico.csv"

data = np.genfromtxt(route, delimiter=",", encoding="utf-8", dtype=str, unpack=True, skip_header=1)

alcaldias = np.unique(data[6])

for alcaldia in alcaldias:
    print(alcaldia)