import pymongo
from password import password

MONGO_URL = f"mongodb+srv://admin:{password}@cluster0.3hpa5li.mongodb.net"

MONGO_BASEDATOS = "sample_training"
MONGO_COLECCION = "zips"

try:
    cliente = pymongo.MongoClient(MONGO_URL, serverSelectionTimeoutMS = 1000)

    baseDatos = cliente[MONGO_BASEDATOS]
    coleccion = baseDatos[MONGO_COLECCION]
    
    datos = {
        "city": "Madrid",
        "zip": "458971",
        "loc": (40.342553, -3.171997),
        "pop": 11111,
        "state": "SP"
    }
    
    coleccion.insert_one(datos)
    
    comprobar = coleccion.find({"city": "Madrid"})
    print(list(comprobar))
    
    cliente.close()
    
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido de carga")
    
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb" + errorConexion)