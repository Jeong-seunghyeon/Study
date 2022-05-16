
import numpy as np

arr1 = np.array([[1, 2, 3],[11, 12, 13],[11, 12, 13]])
arr2 = np.array([[4, 5, 6],[21, 22, 23],[11, 12, 13]])
arr3 = np.array([[4, 5, 6],[21, 22, 23],[11, 12, 13]])
arr4 = np.array([[4, 5, 6],[21, 22, 23],[11, 12, 13]])

print(arr1.shape) # (3, 3) 4개 배열

arr = np.dstack((arr1, arr2, arr3 , arr4))
print(arr)
print(arr.shape)
print("-"*20, str(1))  # 배열 개수 만큼 열 생성

arr = np.stack((arr1, arr2, arr3 , arr4), axis=1)
print(arr)
print(arr.shape)
print("-"*20, str(2)) # 배열 개수 만큼 행 생성

arr = np.stack((arr1, arr2, arr3 , arr4))
print(arr)
print(arr.shape)
print("-"*20, str(3)) # 배열 개수 만큼 면 생성

arr = np.concatenate((arr1, arr2, arr3 , arr4))
print(arr.shape)
print(arr)
print("-"*20, str(4))

arr = np.concatenate((arr1, arr2, arr3 , arr4), axis=1)
print(arr.shape)
print(arr)

print("-"*20, str(5))