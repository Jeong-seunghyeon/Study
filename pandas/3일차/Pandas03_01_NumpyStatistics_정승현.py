import pandas as pd
import numpy as np

vData = pd.read_csv('../_dataSetPandas/gapminder.tsv',sep='\t')



print(vData['lifeExp'])

def datainfo(vData):
    Max = -9999
    Min = 9999
    Sum = 0
    for x in range(len(vData['lifeExp'])):
        if vData['lifeExp'][x] > Max:
            Max = vData['lifeExp'][x]
    for y in range(len(vData['lifeExp'])):
        if vData['lifeExp'][y] < Min:
            Min = vData['lifeExp'][y]
    for z in range(len(vData['lifeExp'])):
        Sum += vData['lifeExp'][z]
    Avg = (Sum/(len(vData)))
    
    print(f"최대값 {Max}")
    print(f"최소값 {Min}")
    print(f"평균값 {Avg.round(3)}")
    print(f"표준편차 {np.ndarray.std(vData['lifeExp'].values).round(3)}")
    
    
datainfo(vData)