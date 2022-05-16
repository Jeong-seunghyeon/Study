vList = [100, 90, 80, 30, 95, 20]

#최대값과 최솟값을 출력.


vMax = -99999
vMin = +99999

for i in vList:
	if vMax < i:
		vMax=i
	
	if vMin > i:
		vMin=i
	
print(vMax, vMin)