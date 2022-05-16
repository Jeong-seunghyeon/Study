import csv, time,datetime
import csv
import time, datetime
import locale
print(locale.getlocale()) 
# locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
locale.setlocale(locale.LC_ALL,'ko_KR.UTF-8')
print(locale.getlocale())


file=open('C:\_pythontest01\_dataSet01/emp2.csv','r')

menu=["사번", "입사일", "사원명"]

emp_csv=csv.reader(file)
#print(type(emp_csv))
#print(emp_csv)

for menuList in menu:
	print("  ",menuList, end="		 ")
print("")
print("="*50)

for empList in emp_csv:
	vDay = datetime.datetime.strptime(empList[4], '%Y-%m-%d')
	print(empList[0] ,"\t\t",vDay.strftime(f"%c"))



