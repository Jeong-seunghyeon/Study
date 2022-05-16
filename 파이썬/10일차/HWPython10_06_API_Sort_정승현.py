#HWPython10_07_ListChk07Sort01_정승현.py

'''
변수 : 값 저장 공긴
함수(매개변수) -> 함수 호출 값 할당.



def myfunc(n):
	return abs(n-50)

thislist = [100,50,65,82,23]
thislist.sort(key = myfunc)
print(thislist)
'''

a = [100,50,65,82,34]

def myfunc(n):
	return abs(n-50)

a.sort(key = myfunc)
print(a)


'''
연습 01
100 - 50 = 50
50 - 50 = 0
65 - 50 = 15
82 - 50 = 32
23 - 50 = -27


연습 02
[50,62,23,82,100]
'''



