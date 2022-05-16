#HWPython10_02_ListW3Chk04_정승현.py

#Add List Items


#연습01(end:append())

a = ['apple','banana','cherry']
a.append('orange')
print(a)
print('-'*40)



#연습02(specified index)
a = ['apple','banana','cherry']
a.insert(1,'orange')
print(a)
print('-'*40)



#연습03(list:extend())
a = ['apple','banana','cherry']
b = ['orange','grape','mango']
a.extend(b)
print(a)
print('-'*40)





#연습04(Any collection type)
a = ['apple','banana','cherry']
b = ('mango','grape')
a.extend(b)
print(a)

