import re
productFile = open('./_dataset01/product.csv','r', encoding='utf8')
productList = productFile.readlines()
a = []
b = []
c = []
for x in range(len(productList)):
	if x == 0:
		pass
	elif x >= 1:
		a.append(productList[x])


def productChk(a):
	for y in range(len(a)):
		if 'Chair' in a[y]:
			b.append(a[y] + ('의자'))
		elif 'Mirror' in a[y]:
			b.append(a[y] + ('거울'))
		elif 'Table' in a[y]:
			b.append(a[y] + ('테이블'))
		elif 'Sofa' in a[y]:
			b.append(a[y] + ('소파'))
		elif 'chair' not in a[y] and 'Mirror' not in a[y] and 'Table' not in a[y] and 'Sofa' not in a[y]:
			b.append(a[y] + ('품목에러 확인'))

productChk(a)
for x in b:
	print(x)














			








