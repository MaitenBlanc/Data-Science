import mysql.connector
from password import password

conexion = mysql.connector.connect(host = "localhost", user = "root", password = password, database="cine")

cursor = conexion.cursor()

sql="SELECT titulo, presupuesto FROM peliculas WHERE presupuesto = (SELECT MAX(presupuesto) FROM peliculas)"

cursor.execute(sql)

for titulo, presupuesto in cursor:
    print("Película más cara:")
    print(f"- {titulo}")
    print(f"- ${presupuesto}")

cursor.close()