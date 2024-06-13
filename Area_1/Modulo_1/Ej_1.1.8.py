peso = float(input("Ingrese peso (kg): "));
estatura = float(input("Ingrese estatura (m): "));

imc = peso / pow(estatura, 2);

print("Tu índice de masa corporal es ", round(imc, 2));