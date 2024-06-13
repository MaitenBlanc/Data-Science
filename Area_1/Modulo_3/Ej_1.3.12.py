mezcla = {"azul", "verde", 1, 6, "rojo", 3, 3, "verde", "azul", 1, "blanco"};

numero = int(input("Ingrese un número para agregar la conjunto: "));

mezcla.remove(3);
mezcla.update(["negro", numero]);

print(mezcla);