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


print(fishData)
print(fish_target)
