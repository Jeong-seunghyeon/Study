import pandas as pd
import numpy as np

class FishData:
    def __init__(self, file='./_DataSetMLDL/Fish.csv'):
        header = []
        self.fishObj = pd.read_csv(file)
        self.alldata = self.fishObj.values.tolist()
        header.append(self.fishObj.columns)
        self.header = header
        self.fishSpecies = self.fishObj['Species'].unique()
    def getFeatureList(self,*args):
        return self.fishObj[['Species',*args]]
    def getSpeciesData(self, argSpecies, *argFishList):
        breamData = []
        lengthWeightData = []
        for x in range(len(self.fishObj)):
            if self.fishObj['Species'][x] == argSpecies:
                breamData.append(self.fishObj[['Species',*argFishList]].values[x])
                lengthWeightData.append(self.fishObj[[*argFishList]].values[x])
        lengthWeightData = np.array(lengthWeightData)
        breamData = np.array(breamData)
                
                
        return lengthWeightData