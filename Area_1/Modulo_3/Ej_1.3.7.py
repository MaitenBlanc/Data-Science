colores = ["rojo","verde","amarillo","azul","blanco","negro"];

color = input("Ingrese el color que desea buscar: ");
color = color.lower();

if color in colores:
    i = colores.index(color);
    print(f"El color {color} está en la posición {i}.");
else:
    print(f"El color {color} no está en la lista.");

