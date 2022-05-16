#HWPython12_02_MemberV02_Step02_정승현.py


menu    = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = ['1','2','3','9']
userList = []
temp = []


while True:
	print('='*20,'메뉴선택','='*20)
	print(menu)
	print('='*50)
	num = input("		메뉴의 번호를 선택해 주세요 : ")

	if int(num) == 1:
		print('		1. 회원가입 알고리즘이 Chk')
		temp.append(input('		ID      : ')),
		temp.append(input('		PWD     : ')),
		temp.append(input('		NAME    : ')),
		temp.append(input('		EMAIL   : ')),
		temp.append(input('		PHONE   : ')),
		temp.append(input('		ADDRESS : '))
		userList.append(temp)
		for x in userList:
			print(x)
		print('현재 회원 수는 ',len(userList),'명입니다.')
		temp.clear()                                     # 클리어를 사용해서 내용은 사라지고 [] 만 남아있다. 따라서 append를 할때 남아있는
														 # []에 입력값이 들어가기 때문에 똑같은 입력값이 계속 반복된다

		
		
	elif int(num) == 2:
		print('2. 로그인 알고리즘이 Chk')
	elif int(num) == 3:
		print('3. 회원목록 알고리즘이 Chk')
	elif int(num) == 9:
		print('종료합니다')
		break
exit()