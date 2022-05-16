#HWPython10_10_ListW3Chk10Copy_정승현.py

#연습 01
a = ['apple','banana','cherry']
b = ['apple','banana','cherry']

print(id(a))
print(id(b))

c = a
print(id(a))
print(id(c))

d = a.copy()
print(id(a))
print(id(d))

#연습 02

e = list(['apple','banana','cherry'])
f = list(['apple','banana','cherry'])

print(id(e))
print(id(f))
