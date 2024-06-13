peliculas = ["El Padrino", "Tiburón", "Los Cazafantasmas", "El Exorcista", "Pulp Fiction", "Star Wars"];
puntuaciones = [];

for i in range(len(peliculas)):
    puntuacion = int(input(f"Puntuación de {peliculas[i]} (1 - 10): "));
    puntuaciones.append(puntuacion);

print("Las películas aprobadas son: ");
for i in range(0, len(puntuaciones)):
    if puntuaciones[i] >= 5:
        print(f"{peliculas[i]}");