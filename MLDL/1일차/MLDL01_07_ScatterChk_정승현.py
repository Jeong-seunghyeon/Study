from FishData import FishData
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fishObj = FishData()
totalData = fishObj.getFeatureList('Length3','Weight')
breamData = fishObj.getSpeciesData('Bream','Length3','Weight')
smeltData = fishObj.getSpeciesData('Smelt','Length3','Weight')
newData = np.array([[22,150]])



print(np.array(breamData))
print(np.array(smeltData))

plt.title('KNN Algorithm')

plt.scatter(np.array(breamData)[:,0], np.array(breamData)[:,1],color='blue', label='Bream')
plt.scatter(np.array(smeltData)[:,0], np.array(smeltData)[:,1],color='Red', label='Smelt')
plt.scatter(newData[:,0], newData[:,1], color='Green', s=200, label='New')
plt.xlabel('Length')
plt.ylabel('Weight')
plt.legend()
plt.show()
