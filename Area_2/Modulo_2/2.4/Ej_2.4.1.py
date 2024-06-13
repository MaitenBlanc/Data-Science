import pymongo
from password import password

MONGO_URL = f"mongodb+srv://admin:{password}@cluster0.3hpa5li.mongodb.net"

MONGO_BASEDATOS = "sample_training"
MONGO_COLECCION = "companies"

try:
    cliente = pymongo.MongoClient(MONGO_URL, serverSelectionTimeoutMS = 1000)

    baseDatos = cliente[MONGO_BASEDATOS]
    coleccion = baseDatos[MONGO_COLECCION]
    
    #Recorremos los objetos que están dentro de la colección
    for documento in coleccion.find():
        print("Compañía: ", documento["name"]);
        print("Cantidad de Empleados: ", documento["number_of_employees"], "\n");
        
    cliente.close()
    
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido de carga")
    
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb" + errorConexion)


