use('sample_restaurants');

// Buscar todos los restaurantes de comida americana
db.restaurants.find({ cuisine: "American" });

// Contar cantidad de elementos
db.restaurants.count({ cuisine: "American" });