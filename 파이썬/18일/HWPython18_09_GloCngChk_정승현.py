#HWPython18_09_GloCngChk_정승현.py

#전역변수 (global variable)
	#함수 외에 선언
	#모든 함수와 공유
# 지역변수 (local variable)
	#함수 내에 선언
	#함수와 생명력을 같이한다.
#함수 안에서 사용하는 매개변수는 지역변수이다.

a=1
def vartest(a):
	a=a+3
	print(a)
	print()


vartest(a)
print(a)
print()
#2. global 명령어 사용하기
	#global 명렁어 : 함수 안에서 함수 밖의 변수를 직접 사용할 때 사용
	#외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니다
a = 1
def vartest():
	global a
	a= a+1
vartest()
print(a)

