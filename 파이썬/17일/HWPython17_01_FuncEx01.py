#ㅗㅉ.py

#함수 형식 01: 기본 함수
# mHello1 함수 생성 ...? 안녕하세요

def mHello1():
	print('안녕하세요')

mHello1()



# 함수 형식 02: 매개변수 >> 호출할 때 값을 할당
# mHello2 함수 생성 ...? 이름값을 받아서 >>> OO님 안녕하세요

def mHello2(vName):
	print(f'{vName}님 안녕하세요')

mHello2('홍길동')
mHello2('정승현')




# 함수형식 03: return
# mHello3 함수 생성 ... 인사말을 반환 받아서 출력
def mHello3():
	return '안녕하세요'

result = mHello3()
print(result)


# 함수 형식 04 : 매개변수, return
#mHello4 함수 생성 ... 이름값을 받아서 인사말과 함께 반환

def mHello4(vName):
	return vName + '님 안녕하세요'

result = mHello4('승현')
print(result)

