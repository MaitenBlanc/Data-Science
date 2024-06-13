from matplotlib import pyplot as plt

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
ventas = []

for mes in meses:
    ventas.append(float(input(f"Introduzca las ventas del mes {mes}: ")))

plt.bar(meses, ventas)
plt.title("Gráfico de Barras de ventas")
plt.grid()
plt.show()