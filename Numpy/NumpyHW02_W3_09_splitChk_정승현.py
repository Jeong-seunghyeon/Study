import numpy as np

# 1번
arr = np.array([1,2,3,4,5,6])

newarr = np.array_split(arr,3)

print(newarr)

# 2번
arr = np.array([1,2,3,4,5,6])

newarr = np.array_split(arr,4)

print(newarr)

# 3번

arr = np.array([1,2,3,4,5,6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])


# 4번

arr = np.array([[1,2], [3,4], [5,6], [7,8], [9,10], [11,12]])

newarr = np.array_split(arr,3)

print(newarr)

# 5번

arr = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])

newarr = np.array_split(arr, 3)

print(newarr)

# 6번

arr = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])

newarr = np.hsplit(arr, 3)

print(newarr)

# 7번
arr = np.array([[1,2,3,1], [4,5,6,1], [7,8,9,1], [10,11,12,1], [13,14,15,1], [16,17,18,1]])

newarr = np.hsplit(arr, 2)

print(newarr)