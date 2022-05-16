#HWPython10_04_ListW3Chk06_정승현.py



#Loop List

#연습 01(Collection Type_item)
a = ['apple','banana','cherry']
for x in a:
	print(x)
print('-'*40)




#연습 02(index_len(),range())
a = ['apple','banana','cherry']
for x in range(len(a)):
	print(a[x])
print('-'*40)




#연습 03(while_len()   비교 증감)
a = ['apple','banana','cherry','mango','grape']
i = 0
while i < len(a):
	print(a[i])
	i = i+1
print('-'*40)




#연습 04 (표현식 Comprehension   for_)
a = ['apple','banana','cherry']
[print(x) for x in a]
b = [x for x in a]
print(b)
print('-'*40)




# List Comprehension
#연습 01(표현식 for__ if)
#[expression for item in iterable if condition == True]
a = ['apple','banana','cherry','kiwi','mango']
b = []

for x in a:
	if 'a' in x:
		b.append(x)

print(b)
print('-'*40)




#연습 02(표현식 for__ if)

a = ['apple','banana','cherry','kiwi','mango']
b = [x for x in a if 'a' in x]
print(b)
print('-'*40)




#연습 03(표현식 for __ if !=)
a = ['apple','banana','cherry','kiwi','mango']
b = [x for x in a if x != "banana"]
print(b)
print('-'*40)





#연습 04(range(10))
b = [x for x in range(10)]
print(b)

print('-'*40)





#연습 05(range(10),if)

b = [x for x in range(10) if x < 5]
print(b)


print('-'*40)




#연습 06(upper)

a = ['apple','banana','cherry','kiwi','mango']
b = [x.upper() for x in a]
print(b)

print('-'*40)




#연습 07(초기화)
a = ['apple','banana','cherry','kiwi','mango']
b = ['hello' for x in a]
print(b)
print('-'*40)





#연습 08(if__else)
a = ['apple','banana','cherry','kiwi','mango']
b = [x if x != 'apple' else 'oragne' for x in a]
print(b)
print('-'*40)