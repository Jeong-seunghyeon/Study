from FishData import FishData
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fishObj = FishData()
totalData = fishObj.getFeatureList('Length2','Weight')
breamData = fishObj.getSpeciesData('Bream','Length2','Weight')
smeltData = fishObj.getSpeciesData('Smelt','Length2','Weight')
newData = np.array([[22,150]])

bream_length = []
bream_weight = []
smelt_length = []
smelt_weight = []

for x in range(len(breamData)):
    bream_length.append(breamData[x][0])
    bream_weight.append(breamData[x][1])
    
for y in range(len(smeltData)):
    smelt_length.append(smeltData[y][0])
    smelt_weight.append(smeltData[y][1])
    
    
print(f"bream_length = {bream_length} \n\n")
print(f"bream_weight = {bream_weight} \n\n")
print(f"smelt_length = {smelt_length} \n\n")
print(f"smelt_weight = {smelt_weight} \n\n")




