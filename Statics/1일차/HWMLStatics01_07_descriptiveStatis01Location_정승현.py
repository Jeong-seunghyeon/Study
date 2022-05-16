dataList = [99,86,87,88,111,86,103,87,94,78,77,85,86]
vcount = []


def funMean(dataList):
	
	print('속도 평균 = ', sum(dataList) // len(dataList))
	

funMean(dataList)

def funMedian(dataList):
	a = sorted(dataList)
	print(a)
	if len(a) % 2 == 1:
		print('속도 중위값 = ', a[len(a)//2])
	else:
		print('속도 중위값 = ', (a[len(a)//2] + a[len(a)//2-1])/2)

funMedian(dataList)


def funMode(dataList):
	for x in range(len(dataList)):
		vcount.append(dataList.count(dataList[x]))
	a = max(vcount)
	if a == vcount[x]:
		print('속도 최빈값 = ', dataList[x],'횟수 : ',a)
	
	

		
funMode(dataList)

