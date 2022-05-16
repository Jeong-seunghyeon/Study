class Employee:
	def __init__(self,no,Name,initday):
		self.no = no
		self.Name = Name
		self.initday = initday
	def payChk(self):
		return 0 
	def getNo(self):
		return self.no
		print(self.no)
	def getName(self):
		return self.Name
		print(self.Name)
	def getInitday(self):
		return self.initday
	def setName(self,Name):
		self.Name = Name
	def setNo(self,no):
		self.no = no
	def setInitday(self,initday):
		self.initday = initday

		
		




class Regular(Employee):
	def __init__(self,no,Name,initday,pay):
		super().setName(Name)
		super().setNo(no)
		super().setInitday(initday)
		self.pay = pay
	def payChk(self):
		return self.pay


class Daily(Employee):
	def __init__(self,no,Name,initday,workday,dailypay):
		super().setName(Name)
		super().setNo(no)
		super().setInitday(initday)
		self.workday = workday
		self.dailypay = dailypay
	def payChk(self):
		return self.workday * self.dailypay

vemployee = [
Regular('r001','오렌지','2021-10-11',200),
Daily('d001','소나무','2021-10-12',9,20),
Regular('r002','오렌지','2021-10-11',200),
Daily('d002','소나무','2021-10-12',9,20),
Regular('r003','오렌지','2021-10-11',200),
Daily('d003','소나무','2021-10-12',9,20)
]
sameValList=["no","devision","name","initday"]


print('='*50)
print('사번	구분	성명	입사일		급여')
print('='*50)
for emp in vemployee:
	for idx,obj in enumerate(sameValList):
		if idx == 1:
			if isinstance(emp,Regular):
				print("일반직",end="	")
			elif isinstance(emp,Daily):
				print("특수직",end="	")
			continue
		value = ("emp.get"+obj[0].upper()+obj[1:]+"()")
		print(eval(value),end="	")
	else:
		print(emp.payChk())

#print(Empobj01.no, Empobj01.Name, Empobj01.initday)
#print(regObj01.no, "일반직", regObj01.getName(), regObj01.initday, regObj01.pay)
#print(dayObj01.no, "특수직", dayObj01.Name, dayObj01.initday, dayObj01.payChk())
