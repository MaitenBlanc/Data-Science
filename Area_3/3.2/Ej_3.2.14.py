import pandas as pd

a = pd.Series([4, 8, 6, 2, 7, 8, 2, 1, 9])
b = []

contador = 0

while contador < len(a) - 1:
    b.append(a[contador] + a[contador + 1])
    contador += 1
    
b = pd.Series(b)
print(b)