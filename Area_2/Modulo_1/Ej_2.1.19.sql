ALTER TABLE personas ADD COLUMN edad INT;

UPDATE personas SET edad = 21 WHERE id = 1;
UPDATE personas SET edad = 45 WHERE id = 2;
UPDATE personas SET edad = 51 WHERE id = 3;
UPDATE personas SET edad = 68 WHERE id = 4;
UPDATE personas SET edad = 30 WHERE id = 5;
UPDATE personas SET edad = 26 WHERE id = 6;

SELECT * FROM personas;