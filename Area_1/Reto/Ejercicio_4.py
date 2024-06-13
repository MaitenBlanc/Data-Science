from pyproj import Transformer
import math;

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

comisarias = {
    "Near North": {
        "latitud": 41.903242,
        "longitud": -87.643352
    },
    "Town Hall": {
        "latitud": 41.947400,
        "longitud": -87.651512
    },
    "Lincoln": {
        "latitud": 41.979550,
        "longitud": -87.692845
    },
    "Distrito: Morgan Park": {
        "latitud": 41.691435,
        "longitud": -87.668520
    },
    "Rogers Park": {
        "latitud": 41.999763,
        "longitud": -87.671324
    }
}

# Crear objeto transformador de coordenadas
transformer = Transformer.from_crs("EPSG:4326", "EPSG:26916");

# Conversión de coordenadas geográficas al sistema de coordenadas EPSG
for comisaria, coordenadas in comisarias.items():
    X, Y = transformer.transform(coordenadas["latitud"], coordenadas["longitud"]);

for delito, coordenadas in delitos.items():
    coords = coordenadas["coordenadas"]
    X, Y = transformer.transform(coords["latitud"], coords["longitud"]);

# Función para calcular las distancias en metros
def calcular_distancia(lat1, lon1, lat2, lon2):
    # Conversión de grados a radianes
    lat1_rad = math.radians(lat1);
    lon1_rad = math.radians(lon1);
    lat2_rad = math.radians(lat2);
    lon2_rad = math.radians(lon2);
    X = lat1_rad - lat2_rad;
    Y = lon1_rad - lon2_rad;

    # Fórmula de la distancia euclidiana en un plano bidimensional
    distancia = math.hypot(X, Y);

    radio_tierra_km = 6371;

    distancia_metros = distancia * radio_tierra_km * 1000;
    return distancia_metros


# Calcular la comisaría más cercana para cada delito
for delito, coord_delito in delitos.items():
    distancia_minima = float("inf");
    comisaria_cercana = None;
    coords = coord_delito["coordenadas"]
    for comisaria, coord_comisaria in comisarias.items():
        distancia = calcular_distancia(coords["latitud"], coords["longitud"],
                                       coord_comisaria["latitud"], coord_comisaria["longitud"]);
        if distancia < distancia_minima:
            distancia_minima = distancia;
            comisaria_cercana = comisaria;

    print(f"Delito {delito}:");
    print(f"Coordenadas del delito: Latitud {coords['latitud']}, Longitud {coords['longitud']}");
    print(f"Comisaría más cercana: {comisaria_cercana}");
    print(f"Distancia euclidiana: {distancia_minima:.3f} metros\n");