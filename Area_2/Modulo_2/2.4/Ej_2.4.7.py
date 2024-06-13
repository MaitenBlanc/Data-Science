from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymongo
from password import password

MONGO_URL = f"mongodb+srv://admin:{password}@cluster0.3hpa5li.mongodb.net"

MONGO_BASEDATOS = "sample_training"
MONGO_COLECCION = "zips"

def mostrarDatos(tabla):
    try:
        cliente = pymongo.MongoClient(MONGO_URL, serverSelectionTimeoutMS=1000)
        baseDatos = cliente[MONGO_BASEDATOS]
        coleccion = baseDatos[MONGO_COLECCION]
        
        for documento in coleccion.find({"city": "BREMEN"}):
            tabla.insert('', 0, text=documento["zip"], values=documento["pop"])
        cliente.close()
        
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo exedido " + errorTiempo)
        
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb " + errorConexion)
        
ventana = Tk()

tabla = ttk.Treeview(ventana, columns=2)
tabla.grid(row=1, column=0, columnspan=2)
tabla.heading("#0", text="Zipcode")
tabla.heading("#1", text="Population")

mostrarDatos(tabla)

ventana.mainloop()



