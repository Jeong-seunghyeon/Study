#HWPython23_05_ClassEx03_정승현.py

result = 0
class CalV01:
	def dbSet(self):
		self.num01 = 0
		self.num02 = 0
	
	def add(self,num1,num2):
		self.num01 += num1
		self.num02 += num2
		return self.num01 + self.num02

cal01 = CalV01()
cal01.dbSet()
result = cal01.add(20,30)
print(f'{cal01.num01}+{cal01.num02}={result}')
#print(cal01.add(20,50))


