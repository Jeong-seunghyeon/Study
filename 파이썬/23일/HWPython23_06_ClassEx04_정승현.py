#HWPython23_06_ClassEx04_정승현.py

result = 0
class CalV01:
	def dbSet(self):
		self.num01 = 0
		self.num02 = 0
	
	def add(self,num1,num2):
		self.num01 += num1
		self.num02 += num2
		return self.num01 + self.num02
	def mul(self,num1,num2):
		self.num01 = num1
		self.num02 = num2
		return self.num01 * self.num02

	def sub(self,num1,num2):
		self.num01 = num1
		self.num02 = num2
		return self.num01 - self.num02

	def div(self,num1,num2):
		self.num01 = num1
		self.num02 = num2
		return self.num01 / self.num02

cal01 = CalV01()
cal01.dbSet()
result1 = cal01.add(100,20)
print(f'{cal01.num01}+{cal01.num02}={result1}')


result2 = cal01.mul(100,20)
print(f'{cal01.num01}*{cal01.num02}={result2}')


result3 = cal01.sub(100,20)
print(f'{cal01.num01}-{cal01.num02}={result3}')

result4 = cal01.div(100,20)
print(f'{cal01.num01}/{cal01.num02}={result4}')

