import csv

regionName = []
regionNum = []
regionMenu = []
vMenu = ['서울 : 108', '대전 : 133', '대구 : 143', '부산 : 159', '광주 : 156', '울산 : 152', 'Q : 종료']
temperRegionFileList = ['seoulNullChk.csv', 'daejeonNullChk.csv', 'daeguNullChk.csv', 
        'busanNullChk.csv', 'gwangjuNullChk.csv', 'ulsanNullChk.csv']
temperFirstLine = []
mydict = {}
a1 = []
a2 = []
a3 = []
for x in regionMenu:
	
	#temperRegionDic = dict(x)
	#print(x)
	a = {x}
	#print(a)

with open('./_dataSetGilBut01/temperRegionChk.csv','r', encoding='949') as rData:
	rData = csv.reader(rData)
	mydict = {rows[0]:rows[1] for rows in rData}
	a1.append(mydict)
	for x in a1:
		a2.append(x.values())
		for y in x:
			a3.append(y)
	for z in a2:
		menu = (list(z))

for firstLine in vMenu:
	if firstLine[5:] in mydict.keys():
		regionMenu.append(firstLine[:2]+':'+firstLine[5:])
		regionNum.append(firstLine[5:])
		regionName.append(firstLine[:2])


print(regionMenu)
print()
print(regionNum)
print()
print(regionName)


	





	
















