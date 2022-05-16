#HWPython23_04_ClassEx02_정승현.py

result = 0
class CalV01:
	def dbSet(self):
		self.result = 0
	
	def add(self,num):
		self.result = self.result + num
		return self.result

cal01 = CalV01()
cal01.dbSet()
print(cal01.add(5))
print(cal01.add(7))


