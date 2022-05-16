#HWPython23_07_ClassEx05_정승현.py

result = 0
class CalV01:
	def __init__(self,n01,n02):
		self.num1 = n01
		self.num2 = n02
	def add(self):
		return self.num1 + self.num2
	
	def div(self):
		return self.num1 / self.num2

	def mul(self):
		return self.num1 * self.num2

	def sub(self):
		return self.num1 - self.num2

cal01 = CalV01(100,20)
result1 = cal01.add()
print(f'{cal01.num1}+{cal01.num2}={result1}')


result2 = cal01.mul()
print(f'{cal01.num1}*{cal01.num2}={result2}')


result3 = cal01.sub()
print(f'{cal01.num1}-{cal01.num2}={result3}')

result4 = cal01.div()
print(f'{cal01.num1}/{cal01.num2}={result4}')

