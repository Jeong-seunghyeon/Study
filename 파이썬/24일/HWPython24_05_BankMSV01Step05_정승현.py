#HWPython24_05_BankMSV01Step05_정승현.py
menu = ['고객번호', '고객이름', '계좌번호', '고객잔액']

class AccountV01DTO:
	bankBalance = 100000
	def __init__(self,costomId,customName,customNumbr, customBalance):
		self.costomId = costomId
		self.customName = customName
		self.customNumbr = customNumbr
		self.customBalance = customBalance
	def getCostomId(self):
		return self.costomId

	def getCustomName(self):
		return self.customName
	
	def getCustomNumbr(self):
		return self.customNumbr

	def getCustomBalance(self):
		return self.customBalance
	
	def setCostomId(self,costomId):
		self.costomId = costomId

	def setCustomName(self,customName):
		self.customName = customName

	def setCustomNumbr(self, customNumbr):
		self.customNumbr = customNumbr

	def setCustomBalance(self, customBalance):
		self.customBalance = customBalance
	
class AccountV01DAO:
	
	AccDtoList = []
	tempList = []
	def __init__(self):
		self.AccDtoList = []
		self.tempList = []
	def DBSet(self):
		try:
			file=open('dataSet03Bank/BankMSDB01.txt', 'r', encoding='UTF8')
		except FileNotFoundError:
			file=open('dataSet03Bank/BankMSDB01.txt', 'w', encoding='UTF8')
			file=open('dataSet03Bank/BankMSDB01.txt', 'r', encoding='UTF8')
		finally:
			bankFile = file.readlines()
			file.close()
		for x in range(len(bankFile)):
			self.tempList = bankFile[x].strip().split(',')
			self.AccDtoList.append(AccountV01DTO(self.tempList[0],self.tempList[1],self.tempList[2],self.tempList[3]))
			AccountV01DTO.bankBalance += int(self.AccDtoList[x].getCustomBalance())
		
	def customSel(self):
		print('='*25,'은행 관리 프로그램 V01','='*25)
		for idx in range(len(self.AccDtoList)):
			print(self.AccDtoList[idx].getCostomId(),'\t',end='')
			print(self.AccDtoList[idx].getCustomName(),'\t',end='')
			print(self.AccDtoList[idx].getCustomNumbr(),'\t',end='')
			print(self.AccDtoList[idx].getCustomBalance(),'\t',end='')
			print()
		print('='*74)
		print()
		print('총 인원수',len(self.AccDtoList),'명/ 은행잔고',format(AccountV01DTO.bankBalance,','),'원')
	
	def vSelect(self):
		print(daoObj.customSel())
		while True:
			for x in range(len(self.AccDtoList)):
				print()
				a = input('고객 번호 입력 [5번 : 종료 / 0번 : 고객List / 9번 : 고객 가입 ] : ')
				print()
				if a == '5' :
					print('시스템을 종료합니다')
					exit()
				elif a == '0':
					print(daoObj.customSel())
				elif a =='9':
					print('고객 가입 Algorithm Chk')
					print(daoObj.customIns())
				elif a == self.AccDtoList[x].getCostomId():
					print('고객번호 : ',self.AccDtoList[x].getCostomId())
					print('고객이름 : ',self.AccDtoList[x].getCustomName())
					print('계좌번호 : ',self.AccDtoList[x].getCustomNumbr())
					print('고객잔액 : ',self.AccDtoList[x].getCustomBalance())
				else:
					print('입력하신 번호를 확인해 주세요.')
		
	def customIns(self):
		self.temp = [0,0,0,0]
		_add = int(self.AccDtoList[len(self.AccDtoList)-1].getCostomId()[-3:]) + 1
		userId = "{0:0>3}".format(str(_add))
		_add1 = int(self.AccDtoList[len(self.AccDtoList)-1].getCustomNumbr()[-3:])+1
		userNumber = "{0:0>3}".format(str(_add1))
		print(self.AccDtoList[(len(self.AccDtoList))-1].getCostomId()[:4]+userId, self.AccDtoList[len(self.AccDtoList)-1].getCustomNumbr()[:-3]+userNumber)
		a = input('고객 이름 : ')
		b = input('초기입금 : ')
		self.temp[0] = (self.AccDtoList[(len(self.AccDtoList))-1].getCostomId()[:4]+userId)
		self.temp[1] = (a)
		self.temp[2] = (self.AccDtoList[len(self.AccDtoList)-1].getCustomNumbr()[:-3]+userNumber)
		self.temp[3] = (b)
		print(self.temp)
		self.AccDtoList.append(AccountV01DTO(self.temp[0],self.temp[1],self.temp[2],self.temp[3]))
		AccountV01DTO.bankBalance += int(self.temp[3])
		self.file1=open('dataSet03Bank/BankMSDB01.txt', 'a', encoding='UTF8')
		tempWrite = ','.join(self.temp)+'\n'
		self.file1.write(tempWrite)
		self.file1.close()


		



daoObj = AccountV01DAO()
daoObj.DBSet()
print(daoObj.vSelect())