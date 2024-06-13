import urllib
import numpy as np
import io

# Para ignorar los certificados
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


url = "https://www.consejotransparencia.cl/transparencia_activa/datoabierto/archivosFiscalizacion/BBDD_Funcionarios_Publicos_2020.csv"

data = urllib.request.urlopen(url)

csv = np.genfromtxt(io.BytesIO(data.read()), delimiter=";", encoding="utf-8", dtype=str, unpack=True)

print(csv)