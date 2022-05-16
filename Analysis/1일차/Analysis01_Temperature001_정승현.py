import csv
f = open('./_dataSetGilBut01/daejeon.csv','r', encoding='949')
data = csv.reader(f,delimiter=',')
for row in data:
	print(row)

f.close()
