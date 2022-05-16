import numpy as np

list01 = [1,2,3,4,5]
list02 = [0,2,4,8,16]

cv01 = np.std(list01)/np.mean(list01)
cv02 = np.std(list02)/np.mean(list02)

print('list01의 변동계수 : ', "%.3f" %cv01)
print('list02의 변동계수 : ', "%.3f" %cv02)