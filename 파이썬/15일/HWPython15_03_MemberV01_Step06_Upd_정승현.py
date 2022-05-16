#\\

menu    = ['1. 회원가입', '2. 로그인', '3. 회원목록', '4. 회원수정',  '5. 회원탈퇴','9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = ['1','2','3','4','5','9']
userList = []
temp = []

def memTitle():
	print('='*30,'메뉴선택','='*30)
	print(menu)
	print('='*70)

def menuSelect(num):
	num = input('번호를 입력해 주세요')
	if num in menuChk:
		return int(num);


def joinChk():
	if len(userList) == 0:
		print('회원가입 먼저 해주세요.\n')
		
	
while True:
	memTitle()
	menuSelect(num)

#회원가입-------------------------------------------------------------------
	if int(num) == 1:
		print('		1. 회원가입 알고리즘이 Chk')
		for x in itemList:
			print(f'\t{x:<10}',end='')
			templist = input()
			temp.append(templist)
		userList.append(temp)

		'''
		temp.append(input('		ID		: ')),
		temp.append(input('		PWD		: ')),
		temp.append(input('		NAME		: ')),
		temp.append(input('		EMAIL		: ')),
		temp.append(input('		PHONE		: ')),
		temp.append(input('		ADDRESS		: '))
		'''
	
		for x in userList:
			print(x)
			temp = []
		print('현재 회원 수는 ',len(userList),'명입니다.')
		
		
#로그인-----------------------------------------------------------------------------
	elif int(num) == 2:
		MemChk = 0
		Chkidx = -1
		if len(userList) == 0:
			joinChk()
		else :
			ID = input ('ID를 입력하세요.')
			PWD = input('PWD를 입력하세요.')
		for idx in range(len(userList)):
			if ID == userList[idx][0]:
				MemChk = 1
				Chkidx = idx
				break
		if MemChk == 1:
			if (userList[Chkidx][1] ==PWD) :
					print(userList[Chkidx][0],'님 로그인 상태입니다.')
			else :
					print('PWD를 확인하세요.')
		else :
			print('ID를 확인하세요.')

			

#회원목록-----------------------------------------------------------------------
	elif int(num) == 3:
		print('^ Member List ! ')
		print('='*70)
		for x in itemList:
				print('{0:<10}'.format(x),end='')
		print()
		print('='*70)
		if userList == []:
			joinChk()
		else:
			for x in userList:
				for y in x:
					print('{0:<10}'.format(y),end='')
				print()
		print('-'*70)
#회원수정------------------------------------------------------------------------
	elif int(num) == 4:
		MemChk = 0
		Chkidx = -1
		if len(userList) == 0:
			print('등록된 회원이 없습니다.')
			joinChk()
		else :
			ID = input ('ID를 입력하세요.')
			PWD = input('PWD를 입력하세요.')
		for idx in range(len(userList)):
			if ID == userList[idx][0]:
				MemChk = 1
				Chkidx = idx
				break
		if MemChk == 1:
			if (userList[Chkidx][1] ==PWD) :
				print(userList[Chkidx])
				for x in range(1,len(itemList)):
					ans = input(itemList[x] + '를 수정하시겠습니까? Y/N : ')
					if ans.upper() == 'Y':
						vx = input('수정하실' +  itemList[x]  +  '를 입력하세요. : ')
						userList[idx][x] = vx
					


				'''
				a = input('PWD를 수정하시겠습니까?   Y/N : ')
				if a.upper() == 'Y' :
					vPWD = 	input('수정하실 PWD를 입력하세요. :')
					userList[Chkidx][1] = vPWD
				b = input('NAME을 수정하시겠습니까? Y/N : ')
				if b.upper() == 'Y' :
					vNAME = input('수정하실 NAME을 입력하세요. :')
					userList[Chkidx][2] = vNAME
				c = input('EMAIL을 수정하시겠습니까? Y/N : ')
				if c.upper() == 'Y' :
					vEMAIL = input('수정하실 EMAIL을 입력하세요. :')
					userList[Chkidx][3] = vEMAIL
				d = input('PHONE을 수정하시겠습니까? Y/N : ')
				if d.upper() == 'Y' :
					vPHONE = input('수정하실 PHONE을 입력하세요. :')
					userList[Chkidx][4] = vPHONE
				e = input('ADDRESS를 수정하시겠습니까? Y/N : ')
				if e.upper() == 'Y' :
					vADDRESS = input('수정하실 ADDRESS를 입력하세요. :')
					userList[Chkidx][5] = vADDRESS
					'''

				print('회원 수정이 완료되었습니다.')
				print(userList[Chkidx])

			else :
					print('PWD를 확인하세요.')
		else :
			print('ID를 확인하세요.')
#회원탈퇴----------------------------------------------------------------------------------------------
	elif int(num) == 5:
		MemChk = 0
		Chkidx = -1
		if len(userList) == 0:
			print('등록된 회원이 없습니다.')
			joinChk()
		else :
			ID = input ('ID를 입력하세요.')
			PWD = input('PWD를 입력하세요.')
		for idx in range(len(userList)):
			if ID == userList[idx][0]:
				MemChk = 1
				Chkidx = idx
				break
		if MemChk == 1:
			if (userList[Chkidx][1] ==PWD) :
					print(userList[Chkidx][0],'님 회원 탈퇴 되었습니다.')
					del userList[Chkidx]
			else :
					print('PWD를 확인하세요.')
		else :
			print('ID를 확인하세요.')
	elif int(num) == 9:
		print('종료합니다')
		break
exit()