INSERT INTO delitos VALUES
("HY411648", "Maltrato doméstico", False, 2, "043XX S WOOD ST", 41.815117, -87.670000),
("HY411595", "Tráfico de drogas", True, 21, "035XX W BARRY AVE", 41.937406, -87.716650),
("HY411435", "Robo en casas", False, 71, "082XX S LOOMIS BLVD", 41.744379, -87.658431),
("HY411662", "Robo por valor menor a 500$", False, 65, "071XX S PULASKI RD", 41.763648, -87.722345);

SELECT * FROM delitos;

INSERT INTO areas_comunitarias VALUES
(1, "Calumet Heights", 2015, 15974, 21032335.12, 50, 100, 42, 30, 365),
(2, "East Side", 2000, 23653, 212335.12, 100, 50, 30, 40, 450),
(3, "Lincoln Park", 2013, 64.320, 21654862.36, 100, 150, 452, 60, 3547),
(4, "Riverdale", 2015, 9809, 21335.12, 40, 80, 42, 80, 180),
(5, "West Englewood", 2000, 45.282, 2140335.12, 90, 130, 58, 10, 158);

SELECT * FROM areas_comunitarias;

INSERT INTO comisarias VALUES
("Near North", "Calumet Heights", "043XX S WOOD ST", "54236998", 41.903242, -87.643352),
("Town Hall", "East Side", "035XX W BARRY AVE", "31268952", 41.947400, -87.651512),
("Lincoln", "Lincoln Park", "082XX S LOOMIS BLVD", "95784236",41.979550, -87.692845),
("Distrito: Morgan Park", "Riverdale", "071XX S PULASKI RD", "6251478",41.691435, -87.668520),
("Rogers Park", "West Englewood", "071XX S PULASKI RD", "3125940",41.999763, -87.671324);

SELECT * FROM comisarias;

INSERT INTO hospitales VALUES
("Chicago Lakeshore Hospital", "Calumet Heights", "043XX S WOOD ST", "43165987", 41.903242, -87.643352),
("Gardiner General Hospital", "East Side", "035XX W BARRY AVE", "57658412", 41.947400, -87.651512),
("Northwestern Memorial Hospital", "Lincoln Park", "082XX S LOOMIS BLVD", "57895440",41.979550, -87.692845),
("Provident Hospital", "Riverdale", "071XX S PULASKI RD", "31587904",41.691435, -87.668520),
("Swedish Hospital", "West Englewood", "071XX S PULASKI RD", "62450831",41.999763, -87.671324);

SELECT * FROM hospitales;

