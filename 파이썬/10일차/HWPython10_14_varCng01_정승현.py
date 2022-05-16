#HWPython10_14_varCng01_정승현.py

'''
변수의 값 서로 변경
a = 100
b = 200


변경전 값 a = 100 b = 200

a = b // a = 200 // b = 200




일반적인  Algorithm
temp = a
a = b
b = temp

변경 후 값 a = 200, b = 100
'''

a = 100
b = 200

print(a)
print(b)

a=b

print(a)
print(b)

a = 100
b = 200
temp = a
a = b
b = temp
print(a)
print(b)
