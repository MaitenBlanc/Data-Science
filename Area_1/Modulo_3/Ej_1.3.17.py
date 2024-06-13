agenda = {};

respuesta = input("¿Desea ingresar datos? (S/N): ");

while respuesta.lower() == "s":
    clave = input("¿Qué dato quieres incluir?: ");
    valor = input(f"Ingrese {clave}: ");
    agenda[clave] = valor;

    respuesta = input("¿Desea ingresar algun dato más? (S/N): ");

print(agenda);