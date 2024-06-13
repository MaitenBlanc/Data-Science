use('sample_restaurants');

// Eliminar todos los restaurantes de Brooklyn
db.restaurants_copy.remove({ borough: "Brooklyn" });