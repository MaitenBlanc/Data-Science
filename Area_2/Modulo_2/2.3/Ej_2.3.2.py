import mysql.connector;
from password import password;

conexion = mysql.connector.connect(host = "localhost", user = "root", password = password, database="cine")

cursor = conexion.cursor()

cursor.execute('CREATE TABLE peliculas'
                '(id INT AUTO_INCREMENT PRIMARY KEY,'
                'titulo VARCHAR(100),'
                'año INT(4),'
                'presupuesto INT)')
