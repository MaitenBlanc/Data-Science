import pandas as pd

datos = {
    "Artículos": ["Art0001", "Art0002", "Art0003", "Art0004", "Art0005"],
    "Pedidos": [325, 125, 205, 54, 186],
    "Entregado": ["S", "S", "N", "N", "S"],
    "Facturación": [8125, 9375, 13325, 18900, 9300]
}

df = pd.DataFrame(datos)

media = df["Facturación"].mean()
varianza = df["Pedidos"].var()
covarianza = df["Pedidos"].cov(df["Facturación"])
media_facturacion = df[df["Entregado"] == "S"][["Pedidos", "Facturación"]].mean()

print(f"a) Media de facturación de los artículos: ${media}")
print(f"b) Varianza de los pedidos: {varianza}")
print(f"c) La covarianza entre los pedidos y la facturación es: {covarianza}")
print(f"d) La media de la facturación y los pedidos entregados es: \n{media_facturacion}")