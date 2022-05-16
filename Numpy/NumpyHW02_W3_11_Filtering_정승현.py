import numpy as np

# 1번

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

# 2번

arr = np.array([41,42,43,44])

filter_arr = []

for x in arr:
    if x > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
        
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# 3번

arr = np.array([1,2,3,4,5,6,7])

filter_arr = []

for x in arr:
    if x %2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
        
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


# 4번

arr = np.array([41,42,43,44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# 5번

arr = np.array([1,2,3,4,5,6,7])

filter_arr = arr% 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)