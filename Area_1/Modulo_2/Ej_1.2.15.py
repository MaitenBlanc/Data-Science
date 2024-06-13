numero = int(input("Ingrese un número positivo: "));

while numero <= 0:
    print("El número debe ser positivo.");
    numero = int(input("Ingrese un número positivo: "));

if numero > 0:
    divisores = "";
    for i in range(1, numero + 1):
            if numero % i == 0:
                divisores += str(i) + " ";
                
print(f"Los divisores de {numero} son: {divisores}");