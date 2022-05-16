import numpy as np

# 1번 
arr1 = np.array([1,2,3])

arr2 = np.array([4,5,6])

arr = np.concatenate((arr1,arr2))


print(arr)

list01 = [1,2,3]
list02 = [4,5,6]

print(list01 + list02)
print(arr1 + arr2)


# 2번

arr3 = np.array([[1,2,3],[1,2,3]])
arr4 = np.array([[4,5,6], [1,2,3]])

arr0 = np.concatenate((arr3, arr4), axis=1)
print(arr0)