from turtle import distance
from FishData import FishData
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


fishObj = FishData()
totalData = fishObj.getFeatureList('Length2','Weight')
breamData = fishObj.getSpeciesData('Bream','Length2','Weight')
smeltData = fishObj.getSpeciesData('Smelt','Length2','Weight')
newData = np.array([[22,150]])


bream_length = list(breamData[:,0])
bream_weight = list(breamData[:,1])

smelt_length = list(smeltData[:,0])
smelt_weight = list(smeltData[:,0])


length = bream_length + smelt_length
weight = bream_weight + smelt_weight

fishData = [[l,w] for l, w in zip(length, weight)]

fish_target = [1]*35 + [0]*14


# print(fishData)
# print(fish_target)

from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier(n_neighbors=5)   # 모델
kn.fit(fishData, fish_target) # 훈련, 학습
result = kn.score(fishData, fish_target) # 모델 정답 예측

print(result)

result02 = kn.predict([[30,600],[10,9]]) # 모델 정답 예측

print(result02)

distances, indexes = kn.kneighbors([[22,150]]) # 거리값, 인덱스 반환
print('==>', distances, indexes)


# [25.4, 242.0]

print(np.sqrt((22-25.4)**2 + (150-242.0)**2))


# plt.title('KNN Algorithm')

# plt.scatter(bream_length, bream_weight, color='Blue', label='Bream')
# plt.scatter(smelt_length, smelt_weight, color='Orange', label='Smelt')
# plt.scatter(newData[:,0], newData[:,1], color='Green', s=200, label='New')
# plt.xlabel('Length')
# plt.ylabel('Weight')
# plt.legend()
# plt.show()
