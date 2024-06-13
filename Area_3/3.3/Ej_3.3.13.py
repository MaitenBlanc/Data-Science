from matplotlib import pyplot as plt
import pandas as pd

route = "C:/Users/maite/OneDrive/Escritorio/Curso-NTT/Area_3/3.3/archivos/apellidos_mas_frecuentes_pais_Argentina.csv"

df = pd.read_csv(route)

plt.boxplot(df['porcentaje_de_poblacion_portadora'], patch_artist=True)
plt.title("Gráfico de Cajas de porcentaje de población portadora")
plt.grid()
plt.show()