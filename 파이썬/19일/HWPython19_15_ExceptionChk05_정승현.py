#HWPython19_15_ExceptionChk05_정승현.py

#1 ZeroDivisionError
try:
	print(100/0)
except:
	print('ZeroDivisionError 발생 확인 !!')
else:
	print('정상적인 Algorithm 실행!! ')

finally:
	print('예외 발생 상관없이 실행 확인')


#2 KeyError
try:
	thisdict = {
	'brand':'ford',
	'model':'mustang',
	'year':1964
	}
	x = thisdict['color']
	print(x)
except:
	print('KeyError 발생 확인 !!')

finally:
	print('예외 발생 상관없이 실행 확인')


#3 Name Error
try:
	print(x)
except:
	print('NameError 발생 확인 !!')
else:
	print('정상적인 Algorithm 실행!! ')


finally:
	print('예외 발생 상관없이 실행 확인')


#4 Type Error
try:
	print(10+'50')
except:
	print('TypeError 발생 확인 !!')
else:
	print('정상적인 Algorithm 실행!! ')

finally:
	print('예외 발생 상관없이 실행 확인')



#5 fileNotFoundError
try:
	f=open('acbd.txt','r')
except:
	print('fileNotFoundError 발생 확인 !!')

else:
	print('정상적인 Algorithm 실행!! ')

finally:
	print('예외 발생 상관없이 실행 확인')