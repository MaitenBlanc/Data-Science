import mysql.connector
from password import password

conexion = mysql.connector.connect(host = "localhost", user = "root", password = password, database="cine")

cursor = conexion.cursor()

sql="SELECT * FROM peliculas WHERE año < 1980"

cursor.execute(sql)

for data in cursor:
    for i in range(len(data)):
        print(f"{data[i]} \t", end="\n")
    
    print(" ", end="\n")
cursor.close()