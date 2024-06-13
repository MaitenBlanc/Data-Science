anio_actual = int(input("Ingrese año actual: "));
anio_a_comparar = int(input("Ingrese otro año: "));

if anio_actual < anio_a_comparar:
    anios = anio_a_comparar - anio_actual;
    print(f"Faltan {anios} años para llegar al año {anio_a_comparar}.");
elif anio_actual > anio_a_comparar:
    anios = anio_actual - anio_a_comparar;
    print(f"Desde el año {anio_a_comparar} han pasado {anios} años.");
else:
    print("Ambos años son el mismo.");