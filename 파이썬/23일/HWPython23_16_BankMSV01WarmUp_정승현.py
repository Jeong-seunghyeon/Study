#bankMSV01.py
'''
실습 ] BankMSV01Step01 ] DTO Chk--------------------------- 

01. BankMSV01DTO.py

menu = ["고객번호", "고객이름", "계좌번호", "고객잔액"]

## class AccountV01DTO:

01. 객체 변수 : customId / customName / customNumbr / customBalance
	-> 생성자에 의해 setting

02. bankBalance = 100000; # 클래스 변수 

03. getter / setter 생성
'''
file=open('dataSet03Bank/BankMSDB01.txt', 'rt', encoding='UTF8')
line=file.readlines()
print(line)
class AccountV01DTO:
	bankBalance = 100000
	def __init__(self,costomId,customName,customNumbr, customBalance):
		self.costomId = costomId
		self.customName = customName
		self.customNumbr = customNumbr
		self.customBalance = customBalance
	def getCostomID(self):
		return self.costomId

	def getCustomName(self):
		return self.customName
	
	def getCustomNumbr(self):
		return self.customNumbr

	def getCustomBalance(self):
		return self.customBalance
	
	def setCostomID(self,costomId):
		self.costomId = costomId

	def setCustomName(self,customName):
		self.customName = customName

	def setCustomNumbr(self, customNumbr):
		self.customNumbr = customNumbr

	def setCustomBalance(self, customBalance):
		self.customBalance = customBalance
	


