import mysql.connector
from password import password

conexion = mysql.connector.connect(host = "localhost", user = "root", password = password, database="cine")

cursor = conexion.cursor()

sql="DELETE FROM peliculas WHERE año < 1980"

cursor.execute(sql)
conexion.commit()

cursor.close()
