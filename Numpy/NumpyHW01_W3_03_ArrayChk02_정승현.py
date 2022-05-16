import numpy as np

arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print('2nd element on 1st row: ', arr1[0,1])



arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print('5th element on 2nd row: ', arr1[1,4])


arr3 = np.array([[[1,2,3],[4,5,6]],
						[[7,8,9],[10,11,12]]])

print(arr3[0,1,2])



arr4 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print('Last element from 2nd dim : ' , arr4[1, -1])


arr5 = np.array([1,2,3,4,5,6,7])

print( arr5[1:5])

arr6 = np.array([1,2,3,4,5,6,7])

print(arr6[-3:-1])


arr7 = np.array([1,2,3,4,5,6,7])

print(arr7[1:5:2])


arr8 = np.array([1,2,3,4,5,6,7])

print(arr8[::2])


arr9 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arr9[1, 1:4])








