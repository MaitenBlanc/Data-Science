from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats

ruta = "./archivos/Tabla.csv"

df = pd.read_csv(ruta, sep=";")

variables = ["A", "E"]

for i in variables:
    CrosstabResult = pd.crosstab(index=df[i], columns=df["B"])
    CrosstabPercent = pd.crosstab(index=df[i], columns=df["B"], normalize="index")
    print(f"{CrosstabPercent}\n")
    
    ChiSqResult = stats.chi2_contingency(CrosstabResult)
    chi2_stat, pvalue, dof, drecuencias = ChiSqResult
    prob = 0.95
    critical = stats.chi2.ppf(prob, df = dof)
    
    if np.abs(chi2_stat) < critical:
        print(f"Variable {i} es dependiente con la target.")

    print(f"El P-Valor del Test Chi2 es: {ChiSqResult[1]}\n")