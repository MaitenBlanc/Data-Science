compra = {};

print("Menu: ");
print("1 - Agregar un producto");
print("2 - Eliminar un producto");
print("3 - Listar todos los productos");
print("4 - Salir");
opcion = int(input("Elija una opción: "));

while opcion != 4:
    if opcion == 1:
        nombre = input("Ingrese producto: ");
        cantidad = input(f"Ingrese cantidad de {nombre}: ");
        
        compra[nombre] = cantidad;
    
    elif opcion == 2:
        print(compra);
        nombre = input("¿Qué producto desea eliminar?: ");

        compra.pop(nombre);
    
    elif opcion == 3:
        print(compra);
    
    opcion = int(input("Elija una opción: "));