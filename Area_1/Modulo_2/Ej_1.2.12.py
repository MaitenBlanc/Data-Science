suma = 0;

numero = input("Ingrese un número positivo: ");

if (numero < "0"):
    print("El número ingresado no es positivo.");
    numero = int(input("Ingrese un número positivo: "));
else:
    for i in range(0, len(numero)):
        suma = suma + int(numero[i]);
    print("La suma de los digitos es:", suma);