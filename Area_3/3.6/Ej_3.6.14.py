import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2

ruta = "./archivos/Tabla.csv"

df = pd.read_csv(ruta, sep=";")

selector_var = SelectKBest(score_func=chi2, k=1)

selector_var.fit_transform(X = df.loc[:, df.columns != 'D'], y = df['D'])

print(f"La variable más relevante es: {selector_var.get_feature_names_out()}")

