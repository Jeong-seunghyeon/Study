


'''
while 1:
    print("*"*6, end=' ')
    print("우송 대학교 과일 판매머신 V01", end=' ')
    print("*"*6)
    print("1. orange     : 1000원")
    print("2. strawberry : 2500원")
    print("3. peach      : 1500원")
    print("4. mango      : 2000원")
    print("5. grape      : 2000원")
    print("6. 종료")
    print("="*50)

a = int(input("구매번호를 입력하세요(1-6)"))

	if a == 1:
		print('\n'+'='*50)
		print("orange는 1000원 입니다.")
		print('='*50)
	elif a == 2:
		print('\n'+'='*50)
		print("strawberry는 2500원 입니다.")
		print('='*50)
	elif a == 3:
		print('\n'+'='*50)
		print("peach는 1500원 입니다.")
		print('='*50)
	elif a == 4:
		print('\n'+'='*50)
		print("mango는 2000원 입니다.")
		print('='*50)
	elif a == 5:
		print('\n'+'='*50)
		print("grape는 2000원 입니다.")
		print('='*50)
	elif a == 6:
		print('\n'+'='*50)
		print("종료")
		print('='*50)
	
	'''

	

menu = ['orange','strawberry','peach','mango','grape','종료']
price = [1000,2500,1500,2000,2011]


while True:
	print('****** 우송 대학교 과일 판매머신 V01 ******')
	idx = 0

while True:
	if(idx==len(menu)-1):
		print('%d.%s'%(idx-1, menu[idx]))
		break

	print('%d.%s:%d 원'%(idx+1,menu[idx],price[idx]))
	idx+=1

print('='*30)

num = int(input('번호를 입력하세요(1~5)'))

if num < len(menu):
	print('%s는:%d원 입니다.\n'%(menu[num-1],price[num-1]))
elif num ==len(menu):
	 break
else:
	print('잘못 입력하셨습니다.')






	
	
   


	


