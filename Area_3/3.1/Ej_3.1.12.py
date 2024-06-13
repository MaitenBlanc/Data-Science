import pandas as pd
import urllib.request

# Para ignorar los certificados
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.consejotransparencia.cl/transparencia_activa/datoabierto/archivosFiscalizacion/BBDD_Funcionarios_Publicos_2020.csv"

data = urllib.request.urlopen(url)

df = pd.read_csv(data, sep=";")

print(df[["ID_Encuestado", "P1_1", "P2_4"]])