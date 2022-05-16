from operator import index
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

fishData = np.column_stack((length, weight))

fish_target = np.concatenate((np.ones(35), np.zeros(14)))


from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier(n_neighbors=5)   # 모델
kn.fit(fishData, fish_target) # 훈련, 학습
result = kn.score(fishData, fish_target) # 모델 정답 예측



result02 = kn.predict(newData) # 모델 정답 예측



distances, indexes = kn.kneighbors([[25,150]])
print('==>', distances, indexes)

fishData = np.array(fishData)

print(fishData[indexes,0])
print(fishData[indexes,1])

result1 = (fishData[indexes,0]-25)**2
result2 = (fishData[indexes,1]-150)**2

result3 = result1 + result2

print(1,np.sqrt(result3))


# plt.title('KNN Algorithm')

# plt.scatter(bream_length, bream_weight, color='Blue', label='Bream')
# plt.scatter(smelt_length, smelt_weight, color='Orange', label='Smelt')
# plt.scatter(newData[:,0], newData[:,1], color='Green', s=200, label='New')
# plt.xlabel('Length')
# plt.ylabel('Weight')
# plt.legend()
# plt.show()
