use('sample_restaurants');

// Buscar todos los restaurantes que están en Brooklyn y tienen comida italiana
db.restaurants.find({ $and: [{ "borough": "Brooklyn" }, { "cuisine": "Italian" }] });

// Contar cantidad de elementos
db.restaurants.count({ $and: [{ "borough": "Brooklyn" }, { "cuisine": "Italian" }] });
