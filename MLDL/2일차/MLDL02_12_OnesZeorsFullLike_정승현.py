import numpy as np

result = np.ones(5)

print(result)
print()
print()


result = np.ones((5,), dtype=int)
print(result)
print()
print()
result = np.ones((2,1))

print(result)
print()

print()

s = (2,2)

result = np.ones(2)

print(result)

print()

x = np.arange(6)
x = x.reshape(2,3)

print(x)
print()

result = np.ones_like(x)

print(result)
print()
result = np.zeros(5)

print(result)
print()
result= np.zeros((5,), dtype=int)
print(result)
print()
result = np.zeros((2,4))
print(result)
print()

x = np.full((2,4),5)

print(x)

y = np.arange(6, dtype=int)
z = np.full_like(y,1)

print(z)

z = np.full_like(x,3)

print(z)