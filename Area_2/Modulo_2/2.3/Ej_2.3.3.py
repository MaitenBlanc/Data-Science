import mysql.connector;
from password import password;

conexion = mysql.connector.connect(host = "localhost", user = "root", password = password, database="cine")

cursor = conexion.cursor()

sql="INSERT INTO cine.peliculas(id, titulo, año, presupuesto) values (%s,%s,%s,%s)"

datos = [
    (1, "El padrino", 1972, 6000000),
    (2, "Tiburón", 1975, 9000000),
    (3, "Los cazafantasmas", 1984, 30000000),
    (4, "El exorcista", 1973, 12000000),
    (5, "Pulp Fiction", 1994, 8000000)
];

cursor.executemany(sql, datos)
conexion.commit()

cursor.close()
conexion.close()

