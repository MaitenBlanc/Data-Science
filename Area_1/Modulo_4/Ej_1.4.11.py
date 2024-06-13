def arroba(texto):
    if '@' in texto:
        return "El texto contiene la @.";
    else:
        return "El texto no contiene la @.";

texto = input("Introduce un texto: ");
print(arroba(texto));
