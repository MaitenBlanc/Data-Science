import password;
import mysql.connector;

conexion = mysql.connector.connect(host = "localhost", user = "root",password = password);
cursor = conexion.cursor();
cursor.execute("CREATE DATABASE cine;");