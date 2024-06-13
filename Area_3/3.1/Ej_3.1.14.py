import pandas as pd

# Para ignorar los certificados
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.consejotransparencia.cl/transparencia_activa/datoabierto/archivosFiscalizacion/BBDD_Funcionarios_Publicos_2020.csv"

df = pd.read_csv(url, sep=";")

nombre = "Funcionarios_Chile.csv"
route = "C:/Users/maite/OneDrive/Escritorio/Curso-NTT/Area_3/archivos/"

df.to_csv(route + nombre, sep=";", encoding="utf-8")

# Comprobar que el archivo se ha guardado
funcionarios = pd.read_csv(route + nombre, sep=";")

print(funcionarios)



