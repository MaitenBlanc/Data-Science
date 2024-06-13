use('sample_restaurants');

// Actualización del restaurante Carvel Ice Cream (Brooklyn a Manhattan).
db.restaurants_copy.updateOne({ name: "Carvel Ice Cream" },
    { $set: { borough: "Manhattan" } });

// Busqueda del dato para comprobar si se ha actualizado correctamente.
db.restaurants_copy.findOne({ name: "Carvel Ice Cream" });



