#HWPython04_17_sumOddEvenEx01_정승현.py
# 문제 01 1~10까지의 합을 출력
# 문제 02 1~ 10까지의 합을 출력
# 문제 03 1~10까지의 짝수합을 출력


sum = 0
for i in range(1, 11):
	sum += i
	print("1~10까지의 합 =",sum)
print("="*30)
...

sum = 0
for i in range(1, 11, 2):
	sum += 2
	print("1~10까지의 홀수 합=",sum)
print("="*30)
...

for i in range(2, 12, 2):
	print(i)
print("="*30)