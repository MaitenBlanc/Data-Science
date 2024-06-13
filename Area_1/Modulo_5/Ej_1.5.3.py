from datetime import date;

fecha = date(2023, 11, 25);
fecha_nueva = fecha.replace(month=12, day=26);

print(f"La fecha original es: {fecha}");
print(f"La fecha nueva es: {fecha_nueva}");


