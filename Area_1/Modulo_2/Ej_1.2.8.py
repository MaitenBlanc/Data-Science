pin_correcto = 1234;

pin = int(input("Ingrese PIN: "));

while pin != pin_correcto:
    print("PIN incorrecto.");
    pin = int(input("Inténtalo de nuevo: "));

print("PIN aceptado.");