import pandas as pd
import numpy as np

list01 = [1,2,3,4,5]
list02 = [0,2,4,8,16]

ser01 = pd.Series(list01)
ser02 = pd.Series(list02)

desc01 = ser01.describe()
desc02 = ser02.describe()

print('list01의 std : ',desc01['std'], 'list01의 mean : ', desc01['mean'])
print('list01의 변동계수 : ', desc01['std']/desc01['mean'])
print('list02의 std : ',desc02['std'], 'list02의 mean : ', desc02['mean'])
print('list02의 변동계수 : ', desc02['std']/desc02['mean'])


