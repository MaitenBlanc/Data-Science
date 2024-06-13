import pandas as pd

ruta = "./archivos/World_Development_Report_2021.csv"
df = pd.read_csv(ruta, sep=',')

df_counted = df['counted'].value_counts(normalize=True)
df_population = df['population'].value_counts(normalize=True)
df_percentage = df['percentage'].value_counts(normalize=True)

df_counted = pd.DataFrame(df_counted)
df_population = pd.DataFrame(df_population)
df_percentage = pd.DataFrame(df_percentage)

df_counted = df_counted.dropna()
df_population = df_population.dropna()
df_percentage = df_percentage.dropna()

print(df_counted)
print(df_population)
print(df_percentage)