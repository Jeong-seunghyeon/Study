#HWPython10_12_ListW3Chk12Count_정승현.py


#연습 01 (fruits 에서 cherry에 개수를 반환 loop문을 이용)

a = ['apple','banana','cherry','cherry','cherry']

b = 0
for x in a:
	if x == 'cherry':
		b += 1
print(b)

	
#연습 02 count 함수 적용

a = ['apple','banana','cherry','cherry','cherry']
print(a.count('cherry'))

