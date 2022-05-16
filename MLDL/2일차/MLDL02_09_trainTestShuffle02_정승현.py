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

train_input = fishData[:35]
train_target = fish_target[:35]

test_input = fishData[35:]
test_target = fish_target[35:]

input_arr = np.array(fishData)
target_arr = np.array(fish_target)

for idx, vData in enumerate(input_arr):
    print(idx, vData)
    
print(input_arr.shape)

print('01.','='*30)
index = np.arange(49)
print(index)
print('02.','='*30)
np.random.shuffle(index)
print(index)
print('03.','='*30)

train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]

print(input_arr[1], train_input[3])
print(input_arr[13], train_input[0])



