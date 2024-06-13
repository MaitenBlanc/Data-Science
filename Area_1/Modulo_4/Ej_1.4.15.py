def suma_digitos(num):
    suma = 0;
    for i in num:
        suma += int(i);
    return suma;

num = input("Ingrese un número: ");
suma = suma_digitos(num);
print(f"La suma de sus digitos es = {suma}");


