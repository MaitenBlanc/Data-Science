# def maximo(a,b):
#     if x>y:
#         return x
#     else:
#         return y

# def minimo(a,b):
#     if x<y:
#         return x
#     else:
#         return y

# x=int(input("Un número: "))

# y=int(input("Otro número: "))

# print(maximo(x-3, minimo(x+2, y-5)))

# max(2, min(7, -4))
# max(2, -4);


def maximo(x,y):
    if x>y:
        return x
    else:
        return y

def minimo(x,y):
    if x<y:
        return x
    else:
        return y

x=int(input("Un número: "))
y=int(input("Otro número: "))

print(maximo(x-3, minimo(x+2, y-5)))