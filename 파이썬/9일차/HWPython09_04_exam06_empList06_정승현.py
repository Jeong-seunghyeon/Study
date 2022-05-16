#HWPython09_04_exam06_empList06_정승현.py

'''
검색할 직위를 입력하세요 : MANAGER, SALESMAN
[3]
직업이 MANAGER, SALESMAN 직원 리스트.

--------------------------------
이름 직위 급여
--------------------------------

'''

import csv
file = open('./_dataSet01/emp2.csv','r')
emp_csv = csv.reader(file)
list_emp=list(emp_csv)


'''
a = str(input('검색할 지위를 입력하세요.:'))
a1,a2 = a.split(',')

print('-'*30)
print('이름\t직위\t급여\t')
print('-'*30)
for x in range(len(list_emp)):
	if list_emp[x][2] == a1.upper().strip():
		print(f'{list_emp[x][1]}\t{list_emp[x][2]}\t{list_emp[x][-3]}')
	elif list_emp[x][2] == a2.upper().strip():
		print(f'{list_emp[x][1]}\t{list_emp[x][2]}\t{list_emp[x][-3]}')
'''
a = str(input('검색할 지위를 입력하세요.:').upper())
a1 = a.split(',')
print('-'*30)
print('이름\t직위\t급여\t')
print('-'*30)
for x in range(len(list_emp)):
	for list_emp[x][2] in a1:
		if list_emp[x][2] == a1:
			print(f'{list_emp[x][1]}\t{list_emp[x][2]}\t{list_emp[x][-3]}')
