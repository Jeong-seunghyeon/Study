import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
print()
print()

arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr1 = arr1.reshape(2,3,2)

print(newarr1)
print()
print()
arr2 = np.array([1,2,3,4,5,6,7,8])

print(arr2.reshape(2,4).base)
print()
print()

arr3 = np.array([1,2,3,4,5,6,7,8])

newarr3 = arr3.reshape(2,2,-1)

print(newarr3)
print()
print()

arr4 = np.array([[1,2,3],[4,5,6]])

newarr4 = arr4.reshape(-1)

print(newarr4)