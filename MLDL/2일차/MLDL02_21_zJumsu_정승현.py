from operator import index
from statistics import mean
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

fishData = np.array(fishData)




from sklearn.model_selection import train_test_split


train_input, test_input, train_target, test_target = train_test_split(fishData, fish_target, stratify=fish_target, random_state=42)



from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()
kn.fit(train_input, train_target)
vScore = kn.score(test_input, test_target)
# print(vScore)


distances, indexes = kn.kneighbors([[25,150]])
vPredict = kn.predict([[25,150]])
# print(vPredict[0])

# if vPredict == 0:
#     New = '빙어'
#     print(New)
# if vPredict == 1:
#     New = '도미'
#     print(New)

# print(distances, indexes)
# print(len(train_input))
mean = np.mean(train_input, axis=0)
std = np.std(train_input, axis=0)

train_scaled = (train_input - mean)/std
print(train_scaled)
kn.fit(train_scaled, train_target)
new = (test_input - mean)/std
print(new)

vScore = kn.score(new, test_target)
print(vScore)

if vScore == 0:
    print('빙어')
if vScore == 1:
    print('도미')

plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(train_scaled[indexes,0], train_scaled[indexes,1], marker='D')
plt.scatter(new[:,0], new[:,1], marker='^')
plt.xlabel('lenght')
plt.ylabel('weight')
plt.show()