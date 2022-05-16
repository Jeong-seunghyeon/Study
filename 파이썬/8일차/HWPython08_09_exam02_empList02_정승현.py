

import csv
file = open('C:\\_pythontest01\\_dataSet01\\emp2.csv','r')
emp_csv = csv.reader(file)
list_emp=list(emp_csv)

print('='*40)
print('사원명          연봉')
print('='*40)

for x in range(len(list_emp)):
	print(list_emp[x][1],end='\t         ')
	print(list_emp[x][-3])
	