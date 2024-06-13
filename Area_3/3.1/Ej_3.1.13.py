import pandas as pd

# Para ignorar los certificados
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.consejotransparencia.cl/transparencia_activa/datoabierto/archivosFiscalizacion/BBDD_Funcionarios_Publicos_2020.csv"

df = pd.read_csv(url, sep=";")

valor = df.at[319, "P7_4"]

print(f"El valor de la fila 319 de la columna P7_4 es: {valor}")