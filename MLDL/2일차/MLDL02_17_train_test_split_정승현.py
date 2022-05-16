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


fishData = np.array(fishData)


result1 = (fishData[indexes,0]-25)**2
result2 = (fishData[indexes,1]-150)**2

result3 = result1 + result2

from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(fishData, fish_target, random_state=42)

print(f"\n02. {'='*30}")
print(train_input.shape, test_input.shape)
print(train_input[:5])
print(test_input[:5])


print(f"\n03. {'='*30}")
print(train_target.shape, test_target.shape)
print(train_target)
print(test_target)

train_input, test_input, train_target, test_target = train_test_split(fishData, fish_target, stratify=fish_target, random_state=42)

print(f"\n04. {'='*30}")

print(train_target)
print(test_target)
