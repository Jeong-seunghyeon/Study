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
                lengthWeightData = lengthWeightData.tolist()
                breamData = np.array(breamData)
                breamData = breamData.tolist()
                
        return lengthWeightData, breamData
        
    
if __name__=='__main__':
    fish01 = FishData(file='./_DataSetMLDL/Fish.csv')
    '''
    print(fish01.header)
    print(np.array(fish01.alldata).shape)
    print(fish01.fishObj.head(3))
    print(fish01.fishSpecies)
    print(fish01.getFeatureList('Weight','Length1').head(3))
    '''
    lengthWeightData, breamData = fish01.getSpeciesData('Bream','Weight','Length1')
    print(breamData[:3])
    print(lengthWeightData[:3])
    
    
    



