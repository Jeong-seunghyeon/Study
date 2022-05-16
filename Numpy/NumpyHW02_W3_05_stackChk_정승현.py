import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr01 = np.hstack((arr1,arr2))

print(arr01)

arr02 = np.vstack((arr1,arr2))
print(arr02)

arr03 = np.concatenate((arr1,arr2))
print(arr03)

arr1 = np.array([[1,2,3]])
arr2 = np.array([[4,5,6]])
print(arr2.shape)


arr04 = np.concatenate((arr1,arr2))

print(arr04)