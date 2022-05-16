#HWPython18_12_lambdaEx02_정승현.py


# lambda 활용법


x = lambda a: a+10
print(x(5))
print()


x = lambda a,b : a*b
print(x(5,6))
print()


def myfunc(n):
	return lambda a: a*n

mydoubler = myfunc(2)
print(mydoubler(11))
print()


mytripler=myfunc(3)
print(mytripler(11))

