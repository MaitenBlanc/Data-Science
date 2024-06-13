use('sample_restaurants');

// Buscar todos los restaurantes que no estén ni en Staten Island ni en Manhattan
db.restaurants.find({ "borough": { $nin: ["Staten Island", "Manhattan"] } });

// Contar cantidad de elementos
db.restaurants.count({ "borough": { $nin: ["Staten Island", "Manhattan"] } });




