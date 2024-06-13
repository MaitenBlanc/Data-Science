import mysql.connector
from password import password

conexion = mysql.connector.connect(host = "localhost", user = "root", password = password, database="cine")

cursor = conexion.cursor()

sql="SELECT titulo FROM peliculas WHERE titulo LIKE 'E%'"

cursor.execute(sql)

for titulo in cursor:
    print(f"- {titulo[0]}")

cursor.close()