from datetime import datetime, date;

def criminalidad (num_delitos, poblacion):
    if poblacion == 0:
        return None;
    else:
        return (num_delitos/poblacion) * 100.000;

areas = {
    "Área 1": (289, 54991),
    "Área 2": (228, 71942),
    "Área 3": (319, 56362),
    "Área 4": (141, 39493),
    "Área 5": (5, 0)
};

# Cálculo los índices de criminalidad para cada área
indices_criminalidad = {area: criminalidad(delitos, poblacion) for area, (delitos, poblacion) in areas.items()};

# Filtramos los valores None
indices_validos = {area: indice for area, indice in indices_criminalidad.items() if indice is not None};

# Cálculo del máximo, mínimo y medio de los resultados
indice_maximo = max(indices_validos.values());
indice_minimo = min(indices_validos.values());
indice_medio = sum(indices_validos.values()) / len(indices_validos);

print(f"Máximo: {indice_maximo}");
print(f"Mínimo: {indice_minimo}");
print(f"Medio: {indice_medio}");


delitos = {
    "delito_1": {
        "num_caso": "HY411648",
        "descripcion": "Maltrato doméstico",
        "arrestado": False,
        "num_area_comunitaria": 61,
        "cuadra": "043XX S WOOD ST",
        "fecha": "2015-09-05 13:30:00",
        "coordenadas": {
            "latitud": 41.815117,
            "longitud": -87.670000
            }
    },
    "delito_2": {
        "num_caso": "HY411595",
        "descripcion": "Tráfico de drogas",
        "arrestado": True,
        "num_area_comunitaria": 21,
        "cuadra": "035XX W BARRY AVE",
        "fecha": "2015-09-05 12:45:00",
        "coordenadas": {
            "latitud": 41.937406,
            "longitud": -87.716650
            }
    },
    "delito_3": {
        "num_caso": "HY411435",
        "descripcion": "Robo en casas",
        "arrestado": False,
        "num_area_comunitaria": 71,
        "cuadra": "082XX S LOOMIS BLVD",
        "fecha": "2015-09-05 10:55:00",
        "coordenadas": {
            "latitud": 41.744379,
            "longitud": -87.658431
        }
    },
    "delito_4": {
        "num_caso": "HY411662",
        "descripcion": "Robo por valor menor a 500$",
        "arrestado": False,
        "num_area_comunitaria": 65,
        "cuadra": "071XX S PULASKI RD",
        "fecha": "2015-09-05 14:00:00",
        "coordenadas": {
            "latitud": 41.763648,
            "longitud": -87.722345
        }
    }
}

# Convertir la cadena de fecha en un objeto de tipo datetime
for delito, delito_fecha in delitos.items():
    date = delito_fecha["fecha"];
    date_format = "%Y-%m-%d %H:%M:%S";
    delito_fecha["fecha"] = datetime.strptime(date, date_format);

# Ordenar los delitos por fecha en orden descendente
delitos_ordenados = sorted(delitos.values(), key=lambda delito: delito["fecha"], reverse=True);

# Mostrar los delitos ordenados
for delito in delitos_ordenados:
    print(delito);

#  calcular el tiempo promedio (en minutos), entre la consecución de un delito y el siguiente
delitos_ordenados_asc = sorted(delitos.values(), key=lambda delito: delito["fecha"]);
for delito in delitos_ordenados_asc:
    for i in range(0, len(delitos_ordenados_asc) - 1):
        fecha = str(delito["fecha"]);
        fecha_siguiente = i + 1;
        if fecha_siguiente < len(delitos_ordenados_asc):
            delito_siguiente = delitos_ordenados_asc[fecha_siguiente];
            diferencia = delito_siguiente["fecha"] - delito["fecha"];
            tiempo_promedio = diferencia.total_seconds() / 60;
        
    print(f"Tiempo promedio entre delitos: {tiempo_promedio:.1f} minutos");