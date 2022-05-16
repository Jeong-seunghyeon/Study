import pandas as pd

A = ['SCOTT','SMITH','JONES','FORD']
saname = pd.Series(A)

print(saname.index)
print(saname.values)
