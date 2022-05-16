class Person:
	pass

class Child:
	pass

class Child2(Person):
	pass

a = Person()
b = Child()
c = Child()

print(isinstance(a,Person))
print(isinstance(b,Child))
print(isinstance(c,Child2))


'''
# 형변환(객체)
부모 = 자식
자식  != 부모
