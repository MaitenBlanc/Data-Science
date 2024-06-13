import pandas as pd

serie = pd.Series([4, 8, 6, 2, 7, 8, 2, 1, 9],
                index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])

print(f"Elemento del índice e: {serie['e']}")