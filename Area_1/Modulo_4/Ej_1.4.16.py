def es_primo(num):
    if num <= 1:
        return False;
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True;

num = int(input("Ingrese un número (0 para terminar): "));
while num != 0:
    if es_primo(num) == True:
        print(f"El número {num} es primo.");
    else:
        print(f"El número {num} no es primo.");
    
    num = int(input("Ingrese un número (0 para terminar): "));