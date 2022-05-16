import numpy as np
from pandas import array

#1번
arr0 = np.array([1,2,3])
for x in arr0:
    print(x)
    
    
arr = np.array([[1,2,3],[4,5,6]])

# 2번

for x in arr:
    print(x)
    
# 3번
for x in arr:
    for y in x:
        print(y)
        
        
arr1 = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])

# 4번
for x in arr:
    print(x)
    
    
# 5번
for x in arr1:
    for y in x:
        for z in y:
            print(z)