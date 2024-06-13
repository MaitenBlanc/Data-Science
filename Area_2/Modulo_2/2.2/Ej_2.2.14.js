use('sample_restaurants');

// Copia de la colección restaurants
db.restaurants.aggregate([{ $out: "restaurants_copy" }]);