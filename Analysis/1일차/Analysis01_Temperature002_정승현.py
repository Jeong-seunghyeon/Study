import csv
dataSet = open('./_dataSetGilBut01/daejeon.csv','r', encoding='949')
temperatureFile = csv.reader(dataSet)
vHeader = next(temperatureFile)
print(vHeader)

