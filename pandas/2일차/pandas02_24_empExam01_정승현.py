from numpy import empty
import pandas as pd

emp = pd.read_csv('./_dataSetPandas/emp.csv')
print(emp)
print(emp.tail(3))
print(emp.head(3))
print(emp.columns)
print()
print(type(emp))
print()
print(emp[['empno']])
print()
print(type(emp[['empno']]))