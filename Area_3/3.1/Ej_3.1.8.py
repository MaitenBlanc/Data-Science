import numpy as np

route = "C:/Users/maite/OneDrive/Escritorio/Curso-NTT/Area_3/archivos/puntos_de_acceso_wifi_Mexico.csv"

data = np.genfromtxt(route, delimiter=",", encoding="utf-8", dtype=str, unpack=True)

print(data)