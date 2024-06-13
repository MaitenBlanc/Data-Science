def calc_segundos(horas, minutos, segundos):
    print(f"{horas}:{minutos}:{segundos} = {(horas * 3600) + (minutos * 60) + segundos} segundos.");

def calc_horas(segundos):
    print(f"{segundos} = {segundos // 3600} horas, {(segundos % 3600) // 60} minutos, {(segundos % 3600) % 60} segundos.");

print("MENU");
print("1 - Convertir a segundos.");
print("2 - Convertir a horas, minutos y segundos.");
print("0 - Salir.");

opcion = int(input("Elige una opción: "));

while opcion != 0:
    if(opcion == 1):
        horas = int(input("Introduce las horas: "));
        minutos = int(input("Introduce los minutos: "));
        segundos = int(input("Introduce los segundos: "));
        calc_segundos(horas, minutos, segundos);
    elif(opcion == 2):
        segundos = int(input("Introduce los segundos: "));
        calc_horas(segundos);

    opcion = int(input("Elige una opción: "));


