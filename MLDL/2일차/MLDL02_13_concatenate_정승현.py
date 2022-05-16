import numpy as np

a= np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
result = np.concatenate((a, b), axis=0)

print(result)

result = np.concatenate((a,b.T), axis =1)
print(result)

result = np.concatenate((a,b), axis = None)
print(result)