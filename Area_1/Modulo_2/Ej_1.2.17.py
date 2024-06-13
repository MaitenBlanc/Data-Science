num1 = int(input("Ingrese un número: "));
num2 = int(input("Ingrese otro número: "));

while num1 > num2:
    print("El primer número no puede ser mayor que el segundo.");
    num1 = int(input("Ingrese un número: "));
    num2 = int(input("Ingrese otro número: "));

for i in range(num1, num2 + 1, 2):
    print(i);