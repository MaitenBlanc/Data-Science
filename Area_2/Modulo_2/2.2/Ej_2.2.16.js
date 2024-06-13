use('sample_restaurants');

// Actualización de todos los restaurantes a comida Japonesa.
db.restaurants_copy.update({}, { $set: { cuisine: "Japanese" } }, { multi: true });