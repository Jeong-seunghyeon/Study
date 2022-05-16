#HWPython13_12_W3TupleChk05_정승현.py


#연습 01(for 01_collection)
a = ('apple','banana','cherry')
for x in a:
	print(x)
print('-'*20)


#연습 02(index_len,range())
a = ('apple','banana','cherry')
for i in range(len(a)):
	print(a[i])
print('-'*20)



#연습 03(while)
a = ('apple','banana','cherry')
i = 0
while i < len(a):
	print(a[i])
	i = i+1
print('-'*20)


#연습 01(+)
a = ('a','b','c')
b = (1,2,3)
c = a + b
print(c)
print('-'*20)



#연습 02(*)

a = ('apple','banana','cherry')
b = a * 2
print(b)
print('-'*20)

#연습 01(count())
a = (1,3,5,2,4,7,9,8,5,5)
x = a.count(5)
print(x)
print('-'*20)



#연습 02(index())
a = (1,3,5,2,4,7,9,8,5,5)
x = a.index(5)
print(x)

