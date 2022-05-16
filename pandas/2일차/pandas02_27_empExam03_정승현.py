import pandas as pd

emp = pd.read_csv('./_dataSetPandas/emp.csv')
A = ['SCOTT','SMITH','JONES','FORD']
saname = pd.Series(A)


Vempno = emp['ename'].isin(['SCOTT','SMITH','JONES','FORD'])

empno = emp[Vempno]



Vemp = empno[['empno','ename']]

print(Vemp)