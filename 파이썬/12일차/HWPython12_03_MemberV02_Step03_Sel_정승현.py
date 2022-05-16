#HWPython12_03_MemberV02_Step03_Sel_정승현.py


menu    = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = ['1','2','3','9']
userList = []
temp = []


while True:
	print('='*30,'메뉴선택','='*30)
	print(menu)
	print('='*70)
	num = input("		메뉴의 번호를 선택해 주세요 : ")

	if int(num) == 1:
		print('		1. 회원가입 알고리즘이 Chk')
		temp.append(input('		ID		: ')),
		temp.append(input('		PWD		: ')),
		temp.append(input('		NAME		: ')),
		temp.append(input('		EMAIL		: ')),
		temp.append(input('		PHONE		: ')),
		temp.append(input('		ADDRESS		: '))
		userList.append(temp)
		for x in userList:
			print(x)
		print('현재 회원 수는 ',len(userList),'명입니다.')
		temp = []
		
		
	elif int(num) == 2:
		print('2. 로그인 알고리즘이 Chk')
		if len(userList) == 0:
				print('회원가입 먼저 해주세요.')
		else:
			for x in userList:
				ID = input('ID    : ')
				PWD = input('PWD   : ')
				if ID != userList[x][0]:
					print('ID를 확인해 주세요.')
				elif PWD != userList[x][1]:
					print('PWD를 확인해주세요')
				elif ID == userList[x][0] and PWD == userList[x][1]:
					print(userList[x][0],'님 로그인 상태입니다.')
	elif int(num) == 3:
		print('^ Member List ! ')
		print('='*70)
		for x in itemList:
				print('{0:<10}'.format(x),end='')
		print()
		print('='*70)
		if userList == []:
			print('회원가입 먼저 해주세요. ')
		else:
			for x in userList:
				for y in x:
					print('{0:<10}'.format(y),end='')
				print()
		print('-'*70)


	elif int(num) == 9:
		print('종료합니다')
		break
exit()