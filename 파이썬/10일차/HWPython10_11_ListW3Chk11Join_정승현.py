#HWPython10_11_ListW3Chk11Join_정승현.py


#연습 01 (+연산자 사용)
a = ['apple','banana','cherry']
b = [1,2,3]
c = a + b
print(c)




#연습 02 (one by one // append()사용 아이템 별 추가)
a = ['apple','banana','cherry']
b = [1,2,3]

for x in b:
	a.append(x)
print(a)




#연습 03 (extend() // list 별로 추가

a = ['apple','banana','cherry']
b = [1,2,3]

a.extend(b)
print(a)
