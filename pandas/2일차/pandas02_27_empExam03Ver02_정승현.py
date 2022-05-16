import pandas as pd

emp = pd.read_csv('./_dataSetPandas/emp.csv')
A = ['SCOTT','SMITH','JONES','FORD']

for x in range(len(emp)):
    if emp['ename'][x] == 'SCOTT':
        print(emp['ename'][x],emp['empno'][x])
    if emp['ename'][x] == 'SMITH':
        print(emp['ename'][x],emp['empno'][x])
    if emp['ename'][x] == 'JONES':
        print(emp['ename'][x],emp['empno'][x])
    if emp['ename'][x] == 'FORD':
        print(emp['ename'][x],emp['empno'][x])