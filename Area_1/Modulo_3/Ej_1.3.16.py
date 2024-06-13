datos = {};

nombre = datos["nombre"] = input("Ingrese su nombre: ");
apellido = datos["apellido"] = input("Ingrese su apellido: ");
edad = datos["edad"] = input("Ingrese su edad: ");
ciudad = datos["ciudad"] = input("Ingrese ciudad en la que vive: ");
telefono = datos["telefono"] = input("Ingrese su número de teléfono: ");

print(f"{nombre} {apellido} tiene {edad} años, vive en {ciudad} y su número de teléfono es {telefono}.");