from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

ruta = "./archivos/Tabla.csv"

df = pd.read_csv(ruta, sep=";")

data_features = df[["A", "E"]]

figure = plt.figure(figsize = (10, 5))

for i in range(0, len(data_features.columns)):
    figure.add_subplot(2, 2, i + 1)
    sns.histplot(x = df["B"], y = data_features.iloc[:, i])
    plt.title("Relación de " + data_features.columns[i] + " y B")
    plt.ylabel(data_features.columns[i])
    plt.xlabel("B")

plt.show()