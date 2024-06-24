from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

ruta = "./archivos/Tabla.csv"

df = pd.read_csv(ruta, sep=";")

data_features = df[["A", "B", "C", "D"]]

figure = plt.figure(figsize = (10, 15))

for i in range(0, len(data_features.columns)):
    figure.add_subplot(2, 2, i + 1)
    sns.boxplot(x = df["E"], y = data_features.iloc[:, i], showfliers = False)
    plt.title("Relación de " + data_features.columns[i] + " y E")
    plt.ylabel(data_features.columns[i])
    plt.xlabel("E")

plt.show()