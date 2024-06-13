from random import randint

respuesta = [
    "Sí, definitivamente sí.",
    "Probablemente.",
    "Sin duda alguna.",
    "No lo sé, pregunta de nuevo.",
    "Prueba más tarde.",
    "Mejor que no lo sepas.",
    "No, definitivamente no.",
    "No pinta muy bien.",
    "Tengo dudas al respecto."
];

pregunta = input("Ingrese pregunta: ");
resp = respuesta[randint(0, len(respuesta) - 1)];

print("Respuesta: ", resp);