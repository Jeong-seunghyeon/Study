import numpy as np
import math

Bodyheight = [1.62, 1.72, 1.55, 1.7, 1.78, 1.65, 1.64, 1.64, 1.66, 1.74]
result = sum(Bodyheight)
vMean = (result / len(Bodyheight))
MeanDiffer = []
MeanDifferSquare = []
vcount = []


def funMean(Bodyheight):
	result = sum(Bodyheight)
	vMean = (result / len(Bodyheight))
	print('농구선수 키 평균 : ', vMean)

def funMedian(Bodyheight):
	print('농구선수 키 중위값 : ',(Bodyheight[4]+Bodyheight[5])/2)

def funMode(Bodyheight):
	for x in range(len(Bodyheight)):
		vcount.append(Bodyheight.count(Bodyheight[x]))
	a = max(vcount)
	if a == vcount[x]:
		print('농구선수 키 최빈값 = ', Bodyheight[x],'횟수 : ',a)

def funMeanDiffer(funMean):
	for x in range(len(Bodyheight)):
		MeanDiffer.append(Bodyheight[x] - vMean)
	print('농구선수 키 평균 차 : ',MeanDiffer)

def vfunMeanDiffer(funMean):
	for x in range(len(Bodyheight)):
		MeanDiffer.append(Bodyheight[x] - vMean)
	print('농구선수 키 평균 차 합 : ',"%.5f" %sum(MeanDiffer))

def funSum(Bodyheight):
	print('농구선수 키 합 : ', sum(Bodyheight))
	


def funMeanDifferSquare(funMeanDiffer):
	for x in range(len(MeanDiffer)):
		MeanDifferSquare.append(MeanDiffer[x] ** 2)
	print('농구선수 키 평균차제곱 : ',MeanDifferSquare)



def funMeanDifferSquareAvg(funMeanDifferSquare):
	result = sum(MeanDifferSquare)
	vMeanDifferSquareAvg = (result / len(MeanDifferSquare))
	print('농구선수 키 분산 : ',vMeanDifferSquareAvg)


def funVariance(Bodyheight):
	print('농구선수 키 표준편차 : ',np.std(Bodyheight))

def funMax(Bodyheight):
	print('농구선수 키 최대값', max(Bodyheight))

def funMin(Bodyheight):
	print('농구선수 키 최솟값', min(Bodyheight))

def funRange(Bodyheight):
	print('농구선수 키 Range : ', (max(Bodyheight) - min(Bodyheight)))


funMean(Bodyheight)
funMedian(Bodyheight)
funMode(Bodyheight)
funSum(Bodyheight)
funMeanDiffer(funMean)
funMeanDifferSquare(funMeanDiffer)
funMeanDifferSquareAvg(funMeanDifferSquare)
funVariance(Bodyheight)
funMax(Bodyheight)
funMin(Bodyheight)
funRange(Bodyheight)
vfunMeanDiffer(funMean)
print()
print()
print()
print()
print('농구선수 키 평균 : ', np.mean(Bodyheight))
print('농구선수 키 분산 : ', np.var(Bodyheight))
print('농구선수 키 표준편차 : ', np.std(Bodyheight))
print('농구선수 키 최댓값 : ', np.max(Bodyheight))
print('농구선수 키 최솟값 : ', np.min(Bodyheight))
print('농구선수 키 중앙값 : ', np.median(Bodyheight))
print('농구선수 키 range 값 : ', (np.max(Bodyheight) - np.min(Bodyheight)))