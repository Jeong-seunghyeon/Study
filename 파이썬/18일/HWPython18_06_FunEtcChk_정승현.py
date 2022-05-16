#HWPython18_06_FunEtcChk_정승현.py


def add_and_mul(a,b):
	return a+b
	return a*b


result = add_and_mul(3,4)   # a+b 만 넘어와서 7이 나오고 a*b 는 안나온다.
print(result)



def say_nick(nick):
	if nick =='바보':               # 필터링 가능
		return
	print('나의 별명은 %s입니다.'%nick)

say_nick('야호')
say_nick('바보')
