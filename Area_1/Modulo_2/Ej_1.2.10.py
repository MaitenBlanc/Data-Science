cantidad = 0;

ahorro_deseado = float(input("¿Cuánto dinero quieres ahorrar?: $"));

while cantidad < ahorro_deseado :
    dinero = float(input("¿Cuánto dinero metes en la hucha?: $"));
    cantidad = cantidad + dinero;

if cantidad >= ahorro_deseado:
    print("Genial, has conseguido llegar a tu objetivo y has ahorrado $", cantidad);