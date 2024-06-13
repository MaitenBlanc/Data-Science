import csv

with open(".//archivos//apellidos_mas_frecuentes_pais_Argentina.csv", "r") as csv_file:
    lector_csv = csv.reader(csv_file, delimiter = ",")
    
    next(lector_csv, None)
    
    for fila in lector_csv:
        print(fila)
    