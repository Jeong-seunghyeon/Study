#HWPython19_13_ExceptionChk03_정승현.py

#1 ZeroDivisionError
try:
	print(100/0)
	f1=open('asdf.txt','r')
	f1.close()
	X='안녕하세요'
	print(x)
	thisdict = {
	'brand':'ford',
	'model':'mustang',
	'year':1964
	}
	x = thisdict['color']
	print(x)
	print(10+'50')

except ZeroDivisionError:
	print('ZeroDivisionError 발생 확인 !!')

except FileNotFoundError:
	print('FileNotFoundError 발생 확인 !!')

except NameError:
	print('NameError 발생 확인 !!')

except KeyError:
	print('KeyError 발생 확인 !!')

except TypeError:
	print('TypeError 발생 확인 !!')

except:
	print('확인되지 않은 예외 에러 발생')





