result = 0

def add(num):
	global result
	result += num
	return result

print(add(5))
print(add(7))
print(add(10))


'''
함수 : 재사용
클래스 : 틀
메소드 , 클래스 변수
-> 객채생성 후 사용한다.
-> a.메소드, a.변수
-> b.메소드, b.변수

※거푸집 Ex] 풀빵틀 >> 풀빵(객체)
