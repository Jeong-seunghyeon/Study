import numpy as np

class FishData:
    
    def __init__(self, file='./_DataSetMLDL/Fish.csv'):
        with open(file,'r') as fishFile:
            fishData = fishFile.readlines()
            
        self.alldata = [FishIdx.strip().split(',') for FishIdx in fishData]
        self.header = self.alldata.pop(0)
        
        Species = self.alldata[0][0]
        
        self.fishSpecies = [Species]
        for Allidx in self.alldata:
            if Allidx[0] != Species:
                Species = Allidx[0]
                self.fishSpecies.append(Species)
                
if __name__ =='__main__':
    fishObj = FishData()
    print(fishObj.header)
    print(fishObj.fishSpecies)
    print(np.array(fishObj.alldata).shape)
    print(fishObj.alldata[:3])
                
        