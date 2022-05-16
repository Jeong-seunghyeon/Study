import csv
temperRegionFileList = ['seoulNullChk.csv', 'daejeonNullChk.csv', 'daeguNullChk.csv', 
        'busanNullChk.csv', 'gwangjuNullChk.csv']
temperFirstLine = []
for x in temperRegionFileList:
	f = open('./_dataSetGilBut01/'+x,'r', encoding='949')
	data = csv.reader(f)
	data1 = list(data)
	temperFirstLine.append(data1[1])

# MenuSetting01 : 배열에 기술된 파일의 첫행만 추출한다. ==============

print(temperFirstLine)
