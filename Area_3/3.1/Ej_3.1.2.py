import csv

route = "C://Users//maite//OneDrive//Escritorio//Curso-NTT//Area_3//archivos//apellidos_mas_frecuentes_pais_Argentina.csv"

with open(route, "r") as csv_file:
    lector_csv = csv.reader(csv_file, delimiter = ",")
    
    next(lector_csv, None)
    
    print("Apellidos cuyo porcentaje de población sea mayor del 0.1:")
    
    for fila in lector_csv:
        if float(fila[1]) > 0.1:
            print(fila[0])