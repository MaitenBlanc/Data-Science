from password import password
import pymongo

MONGO_URL = f"mongodb+srv://admin:{password}@cluster0.3hpa5li.mongodb.net"

MONGO_BASEDATOS = "delincuencia"
MONGO_COLECCION = "criminales"

try:
    cliente = pymongo.MongoClient(MONGO_URL, serverSelectionTimeoutMS = 1000)

    baseDatos = cliente[MONGO_BASEDATOS]
    coleccion = baseDatos[MONGO_COLECCION]
    
    # Crear DB delincuencia y tabla criminales
    baseDatos.create_collection("criminales")
    
    # Insertar datos en tabla criminales
    datosCriminales = [
        {
            "_id": 1,
            "nombre": "AARON",
            "apellidos": "WILLIAMS-BANKS",
            "cuadra": "072XX S SOUTH SHORE DR",
            "delitos": ["agresión sexual", "robo con violencia"],
            "estatura": 185,
            "peso": 80,
            "f_nacimiento": "1976-03-01T08:00:00Z"
        },
        {
            "_id": 2,
            "nombre": "BRIANNA",
            "apellidos": "SMITH-JONES",
            "cuadra": "014XX W MADISON ST",
            "delitos": ["hurto", "posesión de drogas"],
            "estatura": 160,
            "peso": 65,
            "f_nacimiento": "1989-07-15T08:00:00Z"
        },
        {
            "_id": 3,
            "nombre": "CHARLES",
            "apellidos": "BROWN-DAVIS",
            "cuadra": "085XX N SHERIDAN RD",
            "delitos": ["fraude", "evasión fiscal"],
            "estatura": 175,
            "peso": 78,
            "f_nacimiento": "1982-11-23T08:00:00Z"
        },
        {
            "_id": 4,
            "nombre": "DANIELLE",
            "apellidos": "TAYLOR-HARRIS",
            "cuadra": "032XX W JACKSON BLVD",
            "delitos": ["vandalismo", "robo de identidad"],
            "estatura": 170,
            "peso": 60,
            "f_nacimiento": "1993-04-10T08:00:00Z"
        },
        {
            "_id": 5,
            "nombre": "ETHAN",
            "apellidos": "MOORE-CLARK",
            "cuadra": "019XX N CLARK ST",
            "delitos": ["agresión física", "intento de asesinato"],
            "estatura": 180,
            "peso": 85,
            "f_nacimiento": "1978-09-05T08:00:00Z"
        }
    ]
    
    for criminal in datosCriminales:
        baseDatos.criminales.insert_one(criminal)
    
    # Obtener datos de la tabla criminales entre 2 fechas de nacimiento
    query = {"f_nacimiento": {"$gte": "1980-01-01T08:00:00Z", "$lte": "1999-12-31T08:00:00Z"}}
    resultado = coleccion.find(query)
    for dato in resultado:
        print(dato)
    
    # Encontrar los criminales acusados de robo con violencia
    query = {"delitos": "robo con violencia"}
    resultado = coleccion.find(query)
    for dato in resultado:
        print(dato)
    
    # Buscar los criminales con estatura menor a 180 y peso mayor a 75
    query = {"estatura": {"$lt": 180}, "peso": {"$gt": 75}}
    resultado = coleccion.find(query)
    for dato in resultado:
        print(dato)
    
    cliente.close()
    
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido de carga")
    
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb" + errorConexion)