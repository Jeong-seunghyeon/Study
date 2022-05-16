from statistics import median
import pandas as pd
import numpy as np
dataSet = [1.62, 1.72, 1.55, 1.7, 1.78, 1.65, 1.64, 1.64, 1.66, 1.74, 1.78]
vdataSet = sorted(dataSet)
vdata25 = []
vdata75 = []

def funMedian(vdataSet):
    if (len(vdataSet) /2) == 0:
        median = vdataSet[len(vdataSet)/2], vdataSet[(len(vdataSet)/2)-1]
        vdata25.append(median)
        vdata75.append(median)
        for x in range(len(vdataSet)):
            if vdataSet[x] < median:
                vdata25.append(vdataSet[x])
            elif vdataSet[x] > median:
                vdata75.append(vdataSet[x])
        print('25% 데이터 : ', (vdata25[len(vdata25)//2] + vdata25[(len(vdata25)//2)-1])/2)
        print('75% 데이터 : ', (vdata75[len(vdata75)//2] + vdata75[(len(vdata75)//2)-1])/2)


    elif (len(vdataSet)/2) != 0:
        median = vdataSet[len(vdataSet)//2]
        vdata25.append(median)
        vdata75.append(median)
        for x in range(len(vdataSet)):
            if vdataSet[x] < median:
                vdata25.append(vdataSet[x])
            elif vdataSet[x] > median:
                vdata75.append(vdataSet[x])
        if len(vdata25) %2 == 0:
            print('25% 데이터 : ',  vdata25, (vdata25[len(vdata25)//2] + vdata25[(len(vdata25)//2)-1])/2)
            print('75% 데이터 : ',  vdata75, (vdata75[len(vdata75)//2] + vdata75[(len(vdata75)//2)-1])/2)
        else:
            print('25% 데이터 : ',  vdata25, vdata25[len(vdata25)//2])
            print('75% 데이터 : ',  vdata75, vdata75[len(vdata75)//2])

    
#funMedian(vdataSet)

vMedian = median(dataSet)
vQ1Len = np.percentile(dataSet,[25])
vQ3Len = np.percentile(dataSet,[75])

print('농구선수 키 사분위수 Q2_50% : ', vMedian)
print('농구선수 키 사분위수 Q1_25% : ', vQ1Len)
print('농구선수 키 사분위수 Q3_75% : ', vQ3Len)
print('농구선수 키 사분위 편차 : ', vQ3Len-vQ1Len)

