def media(*numeros):
    cant = len(numeros);
    suma = sum(numeros);
    media = suma / cant;
    print(f"Media = {media}");

media(2,4,3);
media(4,5,10,6,8,20);
media(3,5,7,8);