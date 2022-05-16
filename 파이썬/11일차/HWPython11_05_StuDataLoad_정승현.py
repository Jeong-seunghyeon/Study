import csv
import re

file = open('./_dataSet01/StuDataSet02.csv','r')
stu_csv = csv.reader(file)
regExJuminList=[]

for listemp in stu_csv:
	regExJuminList.append(listemp)

def regExJuminChk(inputChk):
	patt = re.compile(r'(\d{6})-(\d)(\d{6})')
	mapp = patt.search(inputChk[2])
	if mapp:
		return mapp.group(1) + '-' + mapp.group(2)+'******'
	else:
		return '잘못된 번호 입력'
a = list(map(regExJuminChk, regExJuminList))

for y in range(len(regExJuminList)):
	regExJuminList[y][2] = a[y]
try:
	f = open('./_dataSet01/StuDataJuminChk.csv','w')
except:
	f = open('./_dataSet01/StuDataJuminChk.csv','a')
	f = open('./_dataSet01/StuDataJuminChk.csv','w')

#print('이름		주민번호		전화번호')
#print('='*50)

for i in regExJuminList:
	print(f'\t\t {i[1]}\t{i[2]}\t{i[3]}')
	data = ','.join(i)+'\n'
	f.write(data)
f.close

