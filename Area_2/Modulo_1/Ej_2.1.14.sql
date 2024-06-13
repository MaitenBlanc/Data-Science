SELECT sexo, COUNT(*) AS num_trabajadores 
FROM personas 
WHERE trabaja = 'S' 
GROUP BY sexo;