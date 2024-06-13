numero = int(input("Ingrese un número: "));

for i in range(numero, -1, -1):
    if numero > 2:
        if numero % 2 == 0:
            primo = False;
        else:
            primo = True;
    elif numero <= 2:
        print("El número debe ser mayor que 2.");
        numero = int(input("Ingrese otro número: "));

if primo:
    print(f"{numero} es primo.");
else:
    print(f"{numero} NO es primo.");