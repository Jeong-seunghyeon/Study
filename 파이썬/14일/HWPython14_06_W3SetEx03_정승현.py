#HWPython14_06_W3SetEx03_정승현.py
## Join Two Sets

'''
01. union() : returns
02. update() :
03. intersection_update : return X
04. intersection : return
05. symmetric difference_update : 차집합의 여집합. return X
06. symmetric difference : 차집합의 여집합. return
'''


#연습 01 (union()
a = {'a','b','c'}
b = {1,2,3}
c = a.union(b)
print(c)
print('-'*20)



#연습 02 (update)
a = {'a','b','c'}
b = {1,2,3}
a.update(b)
print(a)
print('-'*20)

#연습 03 ()
a = {'apple','banana','cherry'}
b = {'mango','kiwi','apple'}
a.intersection_update(b)
print(a)
print('-'*20)


#연습 04
a = {'apple','banana','cherry'}
b = {'mango','kiwi','apple'}
c = a.intersection(b)
print(c)
print('-'*20)

#연습 05

a = {'apple','banana','cherry'}
b = {'mango','kiwi','apple'}

a.symmetric_difference_update(b)
print(a)
print('-'*20)

#연습 06

a = {'apple','banana','cherry'}
b = {'mango','kiwi','apple'}
c = a.symmetric_difference(b)
print(c)

