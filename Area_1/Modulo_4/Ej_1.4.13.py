def suma():
    lista_numeros = [];
    num = int(input("Ingrese un número (0 para terminar): "));
    while num != 0:
        lista_numeros.append(num);
        num = int(input("Ingrese un número (0 para terminar): "));

    suma = sum(lista_numeros);
    print(f"La suma es {suma}");
    return suma;

resultados = [];

for i in range(0, 3):
    resultado = suma();
    resultados.append(resultado);

maximo = max(resultados);
print(f"El máximo es {maximo}");



