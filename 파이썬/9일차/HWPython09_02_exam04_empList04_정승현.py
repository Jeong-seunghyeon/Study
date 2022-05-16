#HWPython09_02_exam04_empList04_정승현.py

'''검색할 연봉 하한값을 입력하세요 : 2500
   검색할 연봉 상한값을 입력하세요 : 3000
   연봉 2500 ~ 3000 인 사원 리스트.

  이름 연봉

'''

import csv
file = open('./_dataSet01/emp2.csv','r')
emp_csv = csv.reader(file)
list_emp=list(emp_csv)

a = int(input('검색할 연봉의 하한값을 입력하세요.:'))
b = int(input('검색할 연봉의 상한값을 입력하세요.:'))

print(f'\n연봉 {a}~{b}인 사원 리스트')
print('='*30)
print('이름\t연봉')
print('='*30)

for x in range(len(list_emp)):
	if int(list_emp[x][-3]) >= a and int(list_emp[x][-3]) <= b:
		print(f'{list_emp[x][1]}\t{list_emp[x][-3]}')
		
