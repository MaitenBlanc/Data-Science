from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

dict = {
    'D_ejer1':[5, 3, 6, 5],
    'D_ejer2':[4, 5, 7, 8]
}

datos = pd.DataFrame(dict)

media = datos.mean()
cuantiles = datos.quantile([0.50, 0.75])
percentiles = datos.quantile([0.40, 0.90])
desv_tipica = datos.std()
varianza = datos.var()
covarianza = datos.cov()
corr_pearson = datos.corr(method='pearson')
corr_matriz = datos.corr(method='pearson')

mostrar = {
    "headers": ["Media", "Cuantil Q2", "Cuantil Q3", "Percentil 40", "Percentil 90", "Desvicación típica", "Varianza"],
    "D_ejer1": [media['D_ejer1'], cuantiles.loc[0.50]['D_ejer1'], cuantiles.loc[0.75]['D_ejer1'], percentiles.loc[0.40]['D_ejer1'], percentiles.loc[0.90]['D_ejer1'], desv_tipica['D_ejer1'], varianza['D_ejer1']],
    "D_ejer2": [media['D_ejer2'], cuantiles.loc[0.50]['D_ejer2'], cuantiles.loc[0.75]['D_ejer2'],  percentiles.loc[0.40]['D_ejer2'], percentiles.loc[0.90]['D_ejer2'], desv_tipica['D_ejer2'], varianza['D_ejer2']]
}

print(f"{pd.DataFrame(mostrar)} \n")

print(f"Covarianza: \n {covarianza} \n")
print(f"Correlación de Pearson: \n {corr_pearson} \n")
print("Matríz de Correlación de Pearson: ")
plt.figure(figsize=(8, 6))
plt.title("Mapa de correlación de Pearson")
sns.heatmap(corr_matriz, annot= True, cmap = 'coolwarm', vmin= -1, vmax=1, center=0)




