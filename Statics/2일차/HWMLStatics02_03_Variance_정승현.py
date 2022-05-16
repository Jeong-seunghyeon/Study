Bodyheight = [1.62, 1.72, 1.55, 1.7, 1.78, 1.65, 1.64, 1.64, 1.66, 1.74]
result = sum(Bodyheight)
vMean = (result / len(Bodyheight))
MeanDiffer = []
MeanDifferSquare = []


def funMean(Bodyheight):
	result = sum(Bodyheight)
	vMean = (result / len(Bodyheight))
	print('농구선수 키 평균 : ', vMean)




def funMeanDiffer(finMean):
	for x in range(len(Bodyheight)):
		MeanDiffer.append(Bodyheight[x] - vMean)
	print('농구선수 키 평균 차 : ',MeanDiffer)


def funMeanDifferSquare(funMeanDiffer):
	for x in range(len(MeanDiffer)):
		MeanDifferSquare.append(MeanDiffer[x] ** 2)
	print('농구선수 키 평균차제곱 : ',MeanDifferSquare)



def funMeanDifferSquareAvg(funMeanDifferSquare):
	result = sum(MeanDifferSquare)
	vMeanDifferSquareAvg = (result / len(MeanDifferSquare))
	print('농구선수 키 분산 : ',vMeanDifferSquareAvg)



funMean(Bodyheight)
funMeanDiffer(funMean)
funMeanDifferSquare(funMeanDiffer)
funMeanDifferSquareAvg(funMeanDifferSquare)




