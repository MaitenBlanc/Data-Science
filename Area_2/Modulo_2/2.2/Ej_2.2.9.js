use('sample_restaurants');

// Crear nueva colección
db.createCollection('Prueba');

// Incluir documento
db.Prueba.insert({
    "address": {
        "building": "1000",
        "coord": [
            -73.542600,
            40.451258
        ],
        "street": "Millan Bv.",
        "zipcode": "3260"
    },
    "borough": "Concepcion",
    "cuisine": "American",
    "grades": [
        { "date": { "$date": "2014-06-10T00:00:00Z" }, "grade": "A", "score": 5 },
        { "date": { "$date": "2013-06-05T00:00:00Z" }, "grade": "A", "score": 7 },
        { "date": { "$date": "2012-04-13T00:00:00Z" }, "grade": "A", "score": 12 },
        { "date": { "$date": "2011-10-12T00:00:00Z" }, "grade": "A", "score": 12 }
    ],
    "name": "Prueba VSC",
    "restaurant_id": "1354862"
});



