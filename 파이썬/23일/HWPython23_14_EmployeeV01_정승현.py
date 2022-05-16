
class Employee:
	def __init__(self,no,Name,initday):
		self.no = no
		self.Name = Name
		self.initday = initday
	def no(self):
		return f'{self.no}'
		print(self.no)
	def Name(self):
		return f'{self.Name}'
		print(self.Name)
	def initday(self):
		return f'{self.initday}'
		print(self.initday)




class Regular(Employee):
	def __init__(self,no,Name,initday,pay):
		super().__init__(no,Name,initday)
		self.pay = pay
	def pay(self):
		return f'{self}'


class Daily(Employee):
	def __init__(self,no,Name,initday,workday,dailypay):
		super().__init__(no,Name,initday)
		self.workday = workday
		self.dailypay = dailypay
	def PayChk(self):
		return self.workday * self.dailypay


regObj01 = Regular('r001','오렌지','2021-10-11',200)
dayObj01 = Daily('d001','소나무','2021-10-12',9,20)

print('='*30)
print('사번	성명	입사일	급여')
print('='*30)
print(regObj01.no, regObj01.Name, regObj01.initday, regObj01.pay)
print(dayObj01.no, dayObj01.Name, dayObj01.initday, dayObj01.PayChk())
