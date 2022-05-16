#HWPython17_03_AutiMachine_step03V02_정승현.py


menu=['orange','strawberry','peach','mango','grape']
coin=[1000,2500,1500,2000,2000]\

def vChange(vNum):
		money = int(input('코인을 투입하세요. : '))
		print('투입된 금액은', money, '원 입니다.')
		print('=' * 50)
		print(f'선택한 과일 : {num}')
		print('받은 금액' , money)
		print('='*5,'거스름돈','='*5)
		change = money - coin[num-1]
		print('거스름돈은', change, '입니다.')
		a = int(change/5000)
		b = int((change-(a*5000)) / 1000)
		c = int((change-(a*5000 + b*1000)) / 500)
		print('5000원 : ',a,'개')
		print('1000원 : ',b,'개')
		print('500원 : ',c,'개')

while True:
	print('*'*6,'우송 대학교 과일 판매 머신 V01','*'*6)
	for x in range(len(menu)) :
		print(x+1,menu[x],coin[x])
	print('='*50)
	num = int(input('구매하실 번호를 입력하세요'))

	if num == 1:
		print(f'입력하신 번호는{num}입니다.')
		vChange(num)
	elif num == 2:
		print(f'입력하신 번호는 {num} 입니다.')
		vChange(num)
	elif num == 3:
		print(f'입력하신 번호는 {num} 입니다.')
		vChange(num)
	elif num == 4:
		print(f'입력하신 번호는 {num} 입니다.')
		vChange(num)
	elif num == 5:
		print(f'입력하신 번호는 {num} 입니다.')
		vChange(num)
	else :
		print('입력하신 번호를 확인하세요.')
		









		