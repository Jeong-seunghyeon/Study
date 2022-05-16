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
        self.args = args
        self.lengthWeightData = self.fishObj[['Species',*args]]
        return self.fishObj[['Species',*args]]
        
        
                
        
if __name__=='__main__':
    fish01 = FishData(file='./_DataSetMLDL/Fish.csv')
    print(fish01.header)
    print(np.array(fish01.alldata).shape)
    print(fish01.fishObj.head(3))
    print(fish01.fishSpecies)
    fish02 = fish01.getFeatureList()
    print(fish01.getFeatureList('Weight','Length1').head(3))






