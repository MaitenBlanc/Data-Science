def calcular_total(cantidad, porcentaje):
    return (cantidad + (cantidad * (porcentaje / 100)));

cantidad = int(input("Ingrese una cantidad a pagar: "));
porcentaje = float(input("Ingrese un porcentaje de impuestos: "));

print(f"Importe total = ${calcular_total(cantidad, porcentaje)}")