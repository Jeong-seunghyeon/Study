#HWPython08_08_exam01_empList01_정승현.py

'''
01. 파일 오픈
	_dataSet01\emp2.csv
02. read
03. type chk
'''
'''
import csv
file = open('C:/_pythontest01/_dataSet01/emp2.csv','r')
emp_csv = csv.reader(file)¡
print(type(emp_csv))
print(emp_csv)
for empList in emp_csv:
	#print(type(empList))
	print(empList)
'''

import csv
file = open('C:\\_pythontest01\\_dataSet01\\emp2.csv','r')
emp_csv = csv.reader(file)
print(type(emp_csv))
print(emp_csv)

for x in emp_csv:
	print(x[1])
	print(x[3])
	


	