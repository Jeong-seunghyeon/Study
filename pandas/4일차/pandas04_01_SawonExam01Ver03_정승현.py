import pandas as pd
import numpy as np

sawonDB = pd.read_csv('../_dataSetPandas/sawonDB.csv',encoding='utf-8',names=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr'])
gogekDB = pd.read_csv('../_dataSetPandas/gogekDB.csv',encoding='utf-8',names=['gobun','goname','gotel','gojumin','godam'])
deptDB = pd.read_csv('../_dataSetPandas/deptDB.csv',encoding='utf-8',names=['deptno','dname','loc'])

# sawonDB.columns=(['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr'])
# gogekDB.columns=(['gobun','goname','gotel','gojumin','godam'])
# deptDB.columns=(['deptno','dname','loc'])
#print(sawonDB)

#print(sawonDB['sahire'].values)
# 문제 1번 -----------------------------------------------------------------------------------
for x in range(len(sawonDB['sahire'])):
    if sawonDB['sahire'].values[x][:2] == '08':
        print(sawonDB[['sahire','saname']].values[x])
#---------------------------------------------------------------------------------------------

# 문제 2번 -----------------------------------------------------------------------------------
for x in range(len(sawonDB['sahire'])):
    if sawonDB['sahire'].values[x][3:5] == '04':
        print(sawonDB[['sahire','saname']].values[x])

#---------------------------------------------------------------------------------------------

# 문제 3번 -----------------------------------------------------------------------------------
for y in range(len(sawonDB['sabun'])) :
    if int(sawonDB['sabun'].values[y])%2 == 0:
        print(sawonDB[['sabun','saname']].values[y])
        
#---------------------------------------------------------------------------------------------
# 문제 4번 #---------------------------------------------------------------------------------------------
a = []
b = []
c = []
d = []
e = []
for z in range(len(sawonDB['sajob'])):
    if sawonDB['sajob'].values[z] == '회장':
        a.append(sawonDB['sapay'].values[z])
    elif sawonDB['sajob'].values[z] == '부장':
        b.append(sawonDB['sapay'].values[z])
    elif sawonDB['sajob'].values[z] == '과장':
        c.append(sawonDB['sapay'].values[z])
    elif sawonDB['sajob'].values[z] == '대리':
        d.append(sawonDB['sapay'].values[z])
    elif sawonDB['sajob'].values[z] == '사원':
        e.append(sawonDB['sapay'].values[z])

print(f"회장 : {sum(a)/len(a)} \n부장 : {sum(b)/len(b)} \n과장 : {sum(c)/len(c)} \n대리 : {sum(d)/len(d)} \n사원 : {sum(e)/len(e)}")

#---------------------------------------------------------------------------------------------

#문제 5번 ---------------------------------------------------------------------------------------------


man = []
girl = []

for sexIdx in range(len(sawonDB['sasex'])):
    if sawonDB['sasex'].values[sexIdx] == '남자':
        man.append(sawonDB['sapay'].values[sexIdx])
    if sawonDB['sasex'].values[sexIdx] == '여자':
        girl.append(sawonDB['sapay'].values[sexIdx])

print(f"남자 : {sum(man)/len(man)} \n여자 : {sum(girl)/len(girl)}")
#---------------------------------------------------------------------------------------------

#문제 6번 ---------------------------------------------------------------------------------------------

for payIdx in range(len(sawonDB['sapay'])):
    print(sawonDB['sapay'].values[payIdx]*1.1)
#---------------------------------------------------------------------------------------------

#문제 7번 ---------------------------------------------------------------------------------------------
dept = []
for deptIdx in range(len(sawonDB['deptno'])):
    if sawonDB['deptno'].values[deptIdx] == 20:
        dept.append(sawonDB['sapay'].values[deptIdx])

print(f" 관리부 평균연봉 : {sum(dept)/len(dept)}")
        



    

        
        

    