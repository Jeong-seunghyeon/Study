#HWPython18_02_GawiBawiBoGameV02_정승현.py


import random

menu = ['1. 가위', '2. 바위', '3. 보', '4. 반복횟수', '5.종료']
myscore = 0
comscore= 0
draw = 0
totalscore = 0
def Tilte():
	print('='*50)
	print(menu)
	print('='*50)51





comChoice = random.randint(1,3)

while True:
	Tilte()
	comChoice = random.randint(1,3)
	myChoice = input('번호를 입력해 주세요. : ')


	if int(myChoice) == 1:
		print('나의 선택 : 가위 ')
		if int(comChoice) == 1:
			print('Com 선택 : 가위 ')
			print('비겼습니다.')
			draw += 1
			totalscore += 1
			print('총 횟수는', totalscore, '현재 스코어는',myscore,':',comscore,'(나 : 컴퓨터) 비긴횟수는', draw, '입니다.')
		if int(comChoice) == 2:
			print('Com 선택 : 바위 ')
			print('졌습니다.')
			comscore += 1
			totalscore += 1
			print('총 횟수는', totalscore, '현재 스코어는',myscore,':',comscore,'(나 : 컴퓨터) 비긴횟수는', draw, '입니다.')
		if int(comChoice) == 3:
			print('Com 선택 : 보 ')
			print('이겼습니다.')
			myscore += 1
			totalscore += 1
			print('총 횟수는', totalscore, '현재 스코어는',myscore,':',comscore,'(나 : 컴퓨터) 비긴횟수는', draw, '입니다.')
	elif int(myChoice) == 2:
		print('나의 선택 : 바위 ')
		if int(comChoice) == 1:
			print('Com 선택 : 가위 ')
			print('이겼습니다.')
			myscore += 1
			totalscore += 1
			print('총 횟수는', totalscore, '현재 스코어는',myscore,':',comscore,'(나 : 컴퓨터) 비긴횟수는', draw, '입니다.')
		if int(comChoice) == 2:
			print('Com 선택 : 바위 ')
			print('비겼습니다.')
			draw += 1
			totalscore += 1
			print('총 횟수는', totalscore, '현재 스코어는',myscore,':',comscore,'(나 : 컴퓨터) 비긴횟수는', draw, '입니다.')
		if int(comChoice) == 3:
			print('Com 선택 : 보')
			print('졌습니다.')
			comscore += 1
			totalscore += 1
			print('총 횟수는', totalscore, '현재 스코어는',myscore,':',comscore,'(나 : 컴퓨터) 비긴횟수는', draw, '입니다.')
	elif int(myChoice) == 3:
		print('나의 선택 : 보 ')
		if int(comChoice) == 1:
			print('Com 선택 : 가위 ')
			print('졌습니다.')
			comscore += 1
			totalscore += 1
			print('총 횟수는', totalscore, '현재 스코어는',myscore,':',comscore,'(나 : 컴퓨터) 비긴횟수는', draw, '입니다.')
		if int(comChoice) == 2:
			print('Com 선택 : 바위 ')
			print('이겼습니다.')
			myscore += 1
			totalscore += 1
			print('총 횟수는', totalscore, '현재 스코어는',myscore,':',comscore,'(나 : 컴퓨터) 비긴횟수는', draw, '입니다.')
		if int(comChoice) == 3:
			print('Com 선택 : 보 ')
			print('비겼습니다.')
			draw += 1
			totalscore += 1
			print('총 횟수는', totalscore, '현재 스코어는',myscore,':',comscore,'(나 : 컴퓨터) 비긴횟수는', draw, '입니다.')
	elif int(myChoice) == 4:
		print('')
	elif int(myChoice) == 5:
		print('종료합니다')
		exit()
	else :
		print('입력하신 번호를 다시 확인하세요.')
	
