import pandas as pd
import numpy as np

sawonDB = pd.read_csv('../_dataSetPandas/sawonDB.csv',encoding='utf-8',names=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr'])
gogekDB = pd.read_csv('../_dataSetPandas/gogekDB.csv',encoding='utf-8',names=['gobun','goname','gotel','gojumin','godam'])
deptDB = pd.read_csv('../_dataSetPandas/deptDB.csv',encoding='utf-8',names=['deptno','dname','loc'])


print(sawonDB[sawonDB.columns.sort_values()])

a = []
b = []
for x in range(len(sawonDB)):
    if sawonDB['sajob'].values[x] == '사원':
        a.append(sawonDB['sapay'].values[x])
    if sawonDB['sajob'].values[x] == '대리':
        b.append(sawonDB['sapay'].values[x])

if len(a) > 3:
    print(f"사원 : 직원수({len(a)}) 평균급여 {sum(a)/len(a)}")
if len(b) > 3:
    print(f"대리 : 직원수({len(b)}) 평균급여 {sum(b)/len(b)}")
    