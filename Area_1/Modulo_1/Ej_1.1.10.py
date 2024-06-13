# 1 dolar = 0.83 libras
# 1 euro = 0.88 libras

dolares = float(input("Ingrese cantidad de dólares: USD$ "));
euros = float(input("Ingrese cantidad de euros: € "));

dolares_libras = dolares * 0.83;
euros_libras = euros * 0.88;

libras = dolares_libras + euros_libras;

print("Tienes £", libras);