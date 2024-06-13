def es_bisiesto(año):
    if año % 400 == 0 or (año % 4 == 0 and año % 100 != 0):
        return True;
    else:
        return False;

def dias_mes(mes):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31;
    elif mes in [4, 6, 9, 11]:
        return 30;
    elif es_bisiesto(año):
        return 29;
    else:
        return 28;

año = int(input("Ingrese un año: "))
mes = int(input("Ingrese un mes: "))

print(f"El mes tiene {dias_mes(mes)} días.");



