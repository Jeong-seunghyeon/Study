#HWPython13_10_W3TupleChk03_정승현.py


#연습 01(Convert_update)
a = ('apple','banana','cherry')
b = list(a)
b[1] = 'kiwi'
a = tuple(b)
print(a)
print(type(a))
print('-'*15)


#연습 02(Convert_add)
a = ('apple','banana','cherry')
b = list(a)
b.append('orange')
a = tuple(b)
print(a)
print(type(a))
print('-'*15)


#연습03(tuple add)
a = ('apple','banana','cherry')
b = ('orange',)
a += b
print(a)
print('-'*15)



#연습04(Convert_remove)
a = ('apple','banana','cherry')
b = list(a)
b.remove('apple')
a = tuple(b)
print(a)
print('-'*15)

#연습05(delete the tuple_del)
a = ('apple','banana','cherry')
del a
print(a)
