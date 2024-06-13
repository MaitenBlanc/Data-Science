import pandas as pd

a = pd.Series([1, 5, 3, 8])
b = pd.Series([4, 8, 3, 9])

c = pd.Series(a % b)

print(c)