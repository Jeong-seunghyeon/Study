#HWPython13_08_DoitListEx08_정승현.py

a = [1,2,3,1,2,3]
a.remove(3)
print(a)

print('-'*15)

a = [1,2,3]
print(a.pop())
print(a)

print('-'*15)

a = [1,2,3]
a.pop(1)
print(a)

print('-'*15)

a = [1,2,3,1]
print(a.count(1))

print('-'*15)

a = [1,2,3]
a.extend((4,5))
print(a)
a.extend('Nice')
print(a)

print('-'*15)
