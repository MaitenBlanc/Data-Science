import folium;

# Diccionarios de delitos y comisarias
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

# Creación del mapa
mapa = folium.Map(location=[41.864380, -87.672638], zoom_start=4);

# Marcadores para comisarias
for comisaria, coordenadas in comisarias.items():
    folium.Marker(
        location=[coordenadas["latitud"], coordenadas["longitud"]],
        tooltip="Click me!",
        popup=comisaria,
        icon=folium.Icon(color="blue"),
    ).add_to(mapa)
    
# Marcadores para delitos
for delito, detalles in delitos.items():
    coords = detalles["coordenadas"]
    text = f"{detalles['descripcion']} (Caso: {detalles['num_caso']})"
    folium.Marker(
        location=[coords["latitud"], coords["longitud"]],
        tooltip="Click me!",
        popup=text,
        icon=folium.Icon(color="red"),
    ).add_to(mapa)

print(mapa);