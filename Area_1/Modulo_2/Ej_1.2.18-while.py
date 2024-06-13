numero = int(input("Ingrese un número (0 para salir): "));

while numero > 1:
    if numero > 2:
        if numero % 2 == 0:
            print(f"{numero} NO es primo.");
        else:
            print(f"{numero} es primo.");
    elif numero <= 2:
        print("El número debe ser mayor que 2.");
    
    numero = int(input("Ingrese un número (0 para salir): "));