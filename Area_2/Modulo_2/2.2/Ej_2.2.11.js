use('sample_restaurants');

// Buscar todos los restaurantes que están en Brooklyn o tienen comida italiana
db.restaurants.find({ $or: [{ "borough": "Brooklyn" }, { "cuisine": "Italian" }] });

// Contar cantidad de elementos
db.restaurants.count({ $or: [{ "borough": "Brooklyn" }, { "cuisine": "Italian" }] });



