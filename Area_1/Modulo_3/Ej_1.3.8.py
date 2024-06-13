numeros = [1, 2, 3, 16, 18, 21, 25];
numero = int(input("Ingrese un número entre 1 y 30: "));

if numero in numeros:
    print("El número", numero, "pertenece a la lista");
else:
    for i in range(len(numeros)):
        if numeros[i] > numero:
            numeros.insert(i, numero);
            break;
    else:
        numeros.append(numero);

print(numeros);