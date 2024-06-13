SELECT COUNT(*) AS trabajadores, sexo, alta
FROM personas 
WHERE trabaja = 'S'
GROUP BY sexo, alta;