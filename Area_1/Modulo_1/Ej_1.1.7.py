import math;

a = float(input("Ingrese valor de a: "));
b = float(input("Ingrese valor de b: "));
c = float(input("Ingrese valor de c: "));

raiz1 = ((-b) + math.sqrt(b*b - 4*a*c)) / 2*a;
raiz2 = ((-b) - math.sqrt(b*b - 4*a*c)) / 2*a;

print("Valor primera raíz = ", raiz1);
print("Valor segunda raíz = ", raiz2);