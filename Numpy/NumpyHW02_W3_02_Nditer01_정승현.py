import numpy as np

# 문제 1
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

for x in np.nditer(arr):
    print(x)
    
    
# 문제 2

arr1 = np.array([1,2,3])

for x in np.nditer(arr1, flags=['buffered'], op_dtypes=['S']):
    print(x)
    
    
# 문제 3

arr2 = np.array([[1,2,3,4], [5,6,7,8]])

for x in np.nditer(arr2[:, ::2]):
    print(x)