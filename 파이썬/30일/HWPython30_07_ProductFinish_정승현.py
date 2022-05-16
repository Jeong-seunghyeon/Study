import re
import csv


a = []
b = []


productFile = open('./_dataset01/product1.csv','r', encoding='utf8')
productList = productFile.readlines()
for x in productList:
	a.append(x)

del a[0]



def productChk(a):
	for y in range(len(a)):
		aList=a[y].split(',')
		if 'Chair' in a[y]:
			aList.insert(3, '의자')
			b.append(aList)
		elif 'Mirror' in a[y]:
			aList.insert(3, '거울')
			b.append(aList)
		elif 'Table' in a[y]:
			aList.insert(3, '테이블')
			b.append(aList)
		elif 'Sofa' in a[y]:
			aList.insert(3, '소파')
			b.append(aList)
		else:
			aList.insert(3, '품목 미체크 확인')
			b.append(aList)

productChk(a)



productFile = open('./_dataset01/product1Chk01.csv','w', encoding='utf8')
for x in b:
	bStr = ','.join(x)
	productFile.write(bStr)
productFile.close

