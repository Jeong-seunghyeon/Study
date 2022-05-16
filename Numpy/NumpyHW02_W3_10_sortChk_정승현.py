import numpy as np

# 1번

arr = np.array([3,2,0,1])

print(np.sort(arr))

print('*'*20)

# 2번

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

print('*'*20)

# 3번

arr = np.array([True, False, True])

print('*'*20)

print(arr)

# 4번

arr = np.array([[3,2,4],[5,0,1]])

print(np.sort(arr))

print('*'*20)

# 5번

arr = np.array([[1,4],[3,1]])

print(np.sort(arr))
print(np.sort(arr, axis=None))
print(np.sort(arr, axis=0))

print('*'*20)

# 6번

arr = np.array([[2,3,1], [6,4,5]])

print(np.sort(arr)[::-1])

print('*'*20)

# 7번

arr = np.array([[2,3,1], [6,4,5]])

print(np.sort(arr)[:,::-1])

print('*'*20)