import numpy as np

route = "./archivos/puntos_de_acceso_wifi_Mexico.csv"

data = np.genfromtxt(route, delimiter = ",", dtype = str, encoding="utf-8")

print(data)