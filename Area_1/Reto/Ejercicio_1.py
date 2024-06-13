# a)
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
    }
}


# b)
nuevo_delito = {
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

delitos["delito_4"] = nuevo_delito;


# c)
numero_caso = "HY411595";

for delito, datos in delitos.items():
    if datos["num_caso"] == numero_caso:
        datos_caso = datos;
        break

if datos_caso:
    print(f"Datos del caso {numero_caso}:");
    for clave, valor in datos_caso.items():
        print(f"{clave}: {valor}");
else:
    print(f"No se encontró ningún caso con el número {numero_caso}.");

# d)
for delito, datos in delitos.items():
    if datos["num_caso"] == "HY411648":
        datos["arrestado"] = True;
        break

if datos:
    print(f"Actualización de datos del caso HY411648:");
    for clave, valor in datos.items():
        print(f"{clave}: {valor}");