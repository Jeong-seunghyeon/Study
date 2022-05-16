import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



arr = np.arange(10)
print(arr)
np.random.shuffle(arr)
print(arr)

arr = np.arange(9).reshape((3,3))
print(arr)
np.random.shuffle(arr)

print(arr)
