salario_actual = float(input("Ingrese salario actual: $ "));

if (salario_actual < 15000):
    salario_actual = salario_actual + salario_actual * 0.1;
    print("Su nuevo salario es: $",salario_actual);
elif (salario_actual >= 15000 and salario_actual <= 20000):
    salario_actual = salario_actual + salario_actual * 0.05;
    print("Su nuevo salario es: $",salario_actual);
else:
    salario_actual = salario_actual + salario_actual * 0.025;
    print("Su nuevo salario es: $",salario_actual);