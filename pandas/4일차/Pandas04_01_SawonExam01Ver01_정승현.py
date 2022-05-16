import pandas as pd
import numpy as np

sawonDB = pd.read_csv('../_dataSetPandas/sawonDB.csv',encoding='utf-8',names=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr'])
gogekDB = pd.read_csv('../_dataSetPandas/gogekDB.csv',encoding='utf-8',names=['gobun','goname','gotel','gojumin','godam'])
deptDB = pd.read_csv('../_dataSetPandas/deptDB.csv',encoding='utf-8',names=['deptno','dname','loc'])

# sawonDB.columns=(['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr'])
# gogekDB.columns=(['gobun','goname','gotel','gojumin','godam'])
# deptDB.columns=(['deptno','dname','loc'])