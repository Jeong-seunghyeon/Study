import numpy as np

# 1번

arr = np.array([1,2,3])

for idx , x in np.ndenumerate(arr):
    print(idx, x)
    
# 2번

arr1 = np.array([[1,2,3,4], [5,6,7,8]])

for idx, x in np.ndenumerate(arr1):
    print(idx, x)