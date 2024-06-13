meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
        "Agosto","Septiembre","Octubre","Noviembre","Diciembre");

posicion = int(input("Ingrese un mes (1 - 12): "));

while posicion < 1 or posicion > 12:
    print("El mes no existe");
    posicion = int(input("Ingrese un mes (1 - 12): "));

if posicion >= 1 and posicion <= 12:
    print(meses[posicion - 1]);

