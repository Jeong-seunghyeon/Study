import csv, time,datetime
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
	s=empList[4].split("-")
	days=datetime.datetime(int(s[0]),int(s[1]),int(s[2]))
	#print(type(empList))
	print(empList[0],"\t\t" , days.strftime('%Y.%b-%d'), "\t\t",empList[1])
print("="*50)