import numpy as np

a = list(zip([1,2,3],[4,5,6]))
print(a)

b = list(zip([1,2,3],[4,5,6],[7,8,9]))

print(b)

c = list(zip("abc","def"))

print(c)

x = [1,2,3,4]
y = [4,5,6,7]
z = []

for i, j in zip(x,y):
    z.append(i + j)
print(z)

x = [1,2,3,4]
y = [4,5,6,7]
z = np.add(x, y)

print(z)