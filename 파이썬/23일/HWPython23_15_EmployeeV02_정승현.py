class Employee:
	def __init__(self,no,Name,initday):
		self.no = no
		self.Name = Name
		self.initday = initday
	def PayChk(self):
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
	def pay(self):
		return f'{self}'


class Daily(Employee):
	def __init__(self,no,Name,initday,workday,dailypay):
		super().setName(Name)
		super().setNo(no)
		super().setInitday(initday)
		self.workday = workday
		self.dailypay = dailypay
	def PayChk(self):
		return self.workday * self.dailypay

Empobj01 = Employee('r001','오렌지','2021-10-11')
regObj01 = Regular('r001','오렌지','2021-10-11',200)
dayObj01 = Daily('d001','소나무','2021-10-12',9,20)

print('='*30)
print('사번	성명	입사일	급여')
print('='*30)
print(Empobj01.no, Empobj01.Name, Empobj01.initday)
print(regObj01.no, regObj01.getName(), regObj01.initday, regObj01.pay)
print(dayObj01.no, dayObj01.Name, dayObj01.initday, dayObj01.PayChk())
