CREATE SCHEMA criminalidad_chicago;

USE criminalidad_chicago;

CREATE TABLE delitos (
  num_caso VARCHAR(15) PRIMARY KEY NOT NULL,
  descripcion VARCHAR(100) NOT NULL,
  arrestado TINYINT NOT NULL,
  num_area_comunitaria INT NOT NULL,
  cuadra VARCHAR(100) NULL,
  latitud FLOAT NOT NULL,
  longitud FLOAT NOT NULL
);
  
CREATE TABLE areas_comunitarias (
  id_area INT NOT NULL,
  nombre VARCHAR(45) PRIMARY KEY NOT NULL,
  año INT NULL,
  poblacion INT NOT NULL,
  ingresos FLOAT NULL,
  latinos INT NULL,
  negros INT NULL,
  blancos INT NULL,
  asiaticos INT NULL,
  otros INT NULL
);

CREATE TABLE comisarias (
  nombre VARCHAR(50) NOT NULL,
  area_comunitaria INT NULL,
  direccion VARCHAR(100) NOT NULL,
  telefono VARCHAR(20) NOT NULL,
  latitud FLOAT NULL,
  longitud FLOAT NULL,
  FOREIGN KEY (area_comunitaria)
  REFERENCES areas_comunitarias(nombre)
);

CREATE TABLE hospitales (
  nombre VARCHAR(100) NOT NULL,
  area_comunitaria VARCHAR(45) NULL,
  direccion VARCHAR(100) NOT NULL,
  telefono VARCHAR(45) NOT NULL,
  latitud FLOAT NULL,
  longitud FLOAT NULL,
  FOREIGN KEY (area_comunitaria)
  REFERENCES areas_comunitarias(nombre)
);