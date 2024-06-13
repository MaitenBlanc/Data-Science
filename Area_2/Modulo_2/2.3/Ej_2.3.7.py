import mysql.connector
from password import password

conexion = mysql.connector.connect(host = "localhost", user = "root", password = password, database="cine")

cursor = conexion.cursor()

sql="SELECT SUM(presupuesto) AS presupuesto_total FROM peliculas"

cursor.execute(sql)

for presupuesto in cursor:
    print(f"Presupuesto total: ${presupuesto[0]}")

cursor.close()