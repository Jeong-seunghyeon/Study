#HWPython19_10_Chap04_01_정승현.py

#Q1 

def is_odd():
	num = input('숫자를 입력하세요.')
	if int(num) % 2 == 0:
		print('짝수 입니다.')
	else :
		print('홀수 입니다.')
is_odd()

#Q2

def mAvg(*args):
	result = 0
	for i in args:
		result += i
	return result / len(args)

print(mAvg(10,20,30))


#Q3

def mReturn():
	num1 = input('숫자를 입력하세요.')
	num2 = input('숫자를 입력하세요.')
	print(int(num1)+int(num2))
mReturn()



#Q4

print("you", "need", "python")

#Q5

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()


#Q6
Memo = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a')  
f.write(Memo)
f.write("\n")              
f.close()


#Q7

f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()