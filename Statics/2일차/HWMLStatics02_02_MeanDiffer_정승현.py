Bodyheight = [1.62, 1.72, 1.55, 1.7, 1.78, 1.65, 1.64, 1.64, 1.66, 1.74]
result = sum(Bodyheight)
vMean = (result / len(Bodyheight))
MeanDiffer = []

def finMean(Bodyheight):
	result = sum(Bodyheight)
	vMean = (result / len(Bodyheight))
	print('농구선수 키 평균 : ', vMean)



finMean(Bodyheight)


def finMeanDiffer(finMean):
	for x in range(len(Bodyheight)):
		MeanDiffer.append(Bodyheight[x] - vMean)
	print('농구선수 키 평균 차 : ',MeanDiffer)

finMeanDiffer(finMean)

