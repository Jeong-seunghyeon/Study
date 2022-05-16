#HWPython16_07_DoitChap02_01_정승현.py


#연습문제 1
score = [80,75,55]
a = sum(score)
print(a/len(score))

#연습문제 2

Num = int(input('확인할 숫자를 입력하세요'))
if Num % 2 == 1:
	print('홀수')
else :
	print('짝수')

#연습문제 3번, 4번

pin = '881120-1068234'
print(pin[0:6],'\t',pin[7:])
print('홍길동님의 생년월일은 19'+pin[0:2],'년' , pin[2:4],'월',pin[4:6],'일 입니다.')
if pin[7] == '1' or pin[7] == '3' :
	print('남성')
elif pin[7] == '2' or pin [7] == '4' :
	print('여성')
else:
	print('다시 입력해 주세요')

# 연습문제 5번
a = "a:b:c:d"
b = a.replace(':','#')
print(b)
