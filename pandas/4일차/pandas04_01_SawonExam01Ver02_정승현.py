import pandas as pd
import numpy as np

sawonDB = pd.read_csv('../_dataSetPandas/sawonDB.csv',encoding='utf-8',names=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr'])
gogekDB = pd.read_csv('../_dataSetPandas/gogekDB.csv',encoding='utf-8',names=['gobun','goname','gotel','gojumin','godam'])
deptDB = pd.read_csv('../_dataSetPandas/deptDB.csv',encoding='utf-8',names=['deptno','dname','loc'])


print(sawonDB[['sajob','sapay']].groupby(['sajob']).mean())

print(sawonDB[['sasex','sapay']].groupby(['sasex']).mean())


print(sawonDB[['deptno','sapay']].groupby(['deptno']).mean().loc[20])
print(sawonDB[['deptno','sapay']].groupby(['deptno']).mean().iloc[1])

