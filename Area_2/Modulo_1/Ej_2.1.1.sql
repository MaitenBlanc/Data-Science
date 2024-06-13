CREATE TABLE personas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(45),
  apellidos VARCHAR(45),
  sexo VARCHAR(1),
  peso INT,
  alta VARCHAR(1),
  trabaja VARCHAR(1)
  );
  
INSERT INTO personas VALUES 
(1, 'Sara', 'Presa Gracia', 'M', 54, 'N', 'N'),
(2, 'Andrés', 'Soria Prieto', 'H', 88, 'S', 'S'),
(3, 'Luisa', 'Tuno Flores', 'M', 62, 'S', 'S'),
(4, 'Pedro Luis', 'Rubio Moreno', 'H', 112, 'N', 'N'),
(5, 'Ana', 'Sur Requejo', 'M', 92, 'N', 'S');

SELECT nombre, apellidos FROM personas WHERE peso > 80;

