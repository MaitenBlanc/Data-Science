nombre1 = input("Ingrese un nombre: ");
nombre2 = input("Ingrese otro nombre: ");

nombre1 = nombre1.lower();
nombre2 = nombre2.lower();

if(nombre1[0] == nombre2[0]):
    print("Ambos nombres comienzan por la misma letra.");
elif (nombre1[-1] == nombre2[-1]):
    print("Ambos nombres terminan por la misma letra.");
elif (nombre1[0] == nombre2[0]) and (nombre1[-1] == nombre2[-1]):
    print("Ambos nombres comienzan y terminan por la misma letra");
else:
    print("Los nombres no coinciden.");