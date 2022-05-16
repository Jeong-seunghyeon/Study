#HWPython18_04_argsTupleChk_정승현.py

def add_many(*args):
	result=0
	print(args)
	for i in args:
		print(i)
		result = result+ i
	return result



result1 = add_many(1,2)
print('=>합 %d' %result1)


result2 = add_many(1,2,3)
print('=>합 %d' %result2)




def mul_many(*args):
	result=0
	cnt =0
	print(args)
	result=1
	for x in args:
		print(x)
		result *= x
	return result

	
result3 = mul_many(1,2,3)
print('=>곱 %d' %result3)

result4 = mul_many(1,2,3,4,5,6,7)
print('=>곱 %d' %result4)