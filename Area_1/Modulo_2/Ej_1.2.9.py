suma = 0;

num = float(input("Ingrese un número: "));

while num != 0:
    suma = suma + num;
    num = float(input("Ingrese un número: "));

print(f"La suma de los números es = {suma}");