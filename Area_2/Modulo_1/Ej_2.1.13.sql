SELECT FORMAT(AVG(peso), 2) AS peso_medio_hombres 
FROM personas 
WHERE sexo = 'H';