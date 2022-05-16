import pandas as pd

class FishData:
    def __init__(self, file='./_DataSetMLDL/Fish.csv'):
        self.fishObj = pd.read_csv(file)
        return print(self.fishObj)
    def alldata(self):
        a = self.fishObj.values
        return print(a)
    def header(self):
        header = self.fishObj.columns
        return print(header)
    def fishSpecies(self):
        return print(self.fishObj['Species'].unique())
    
fish01 = FishData(file='./_DataSetMLDL/Fish.csv')

fish01.header()

fish01.alldata()

fish01.fishSpecies()



