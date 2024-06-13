colores = ['rojo', 'verde', 'amarillo', 'azul', 'blanco', 'verde', 'rojo', 'rojo', 'verde'];

for i in range (0, len(colores)):
    if colores.count(colores[i]) == 1:
        colores.append(colores[i]);

print(colores);