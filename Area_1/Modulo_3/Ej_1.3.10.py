numeros = (5, 6, 4, 8, 19, 0, 4, 6, 6, 5, 4, 8, 3, 5, 6, 0);

numero = int(input("Ingrese un número: "));

if numero not in numeros:
    print(f"El número {numero} no está en la tupla.");
else:
    cantidad = numeros.count(numero);
    print(f"El número {numero} está {cantidad} veces en la tupla.");