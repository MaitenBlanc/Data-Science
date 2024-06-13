import pymongo
from password import password

MONGO_URL = f"mongodb+srv://admin:{password}@cluster0.3hpa5li.mongodb.net"

MONGO_BASEDATOS = "sample_training"
MONGO_COLECCION = "zips"

try:
    cliente = pymongo.MongoClient(MONGO_URL, serverSelectionTimeoutMS = 1000)

    baseDatos = cliente[MONGO_BASEDATOS]
    coleccion = baseDatos[MONGO_COLECCION]
    
    for documento in coleccion.find({"city": "Madrid"}):
        for key, value in documento.items():
            print(key, ":", value)
    
    cliente.close()
    
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido de carga")
    
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb" + errorConexion)