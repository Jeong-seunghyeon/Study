#HWPython14_08_MemberV02_Step04_Sel_정승현.py

menu    = ['1. 회원가입', '2. 로그인', '3. 회원목록','4.회원탈퇴', '9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = []
userList = []
temp = []


for a in range(len(menu)):
	menuChk.append(menu[a][0])
	print(menuChk)



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
