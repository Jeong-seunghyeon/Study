import pandas as pd
import numpy as np

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
print(df)
print('-'*30)
print(df.dtypes)
print('-'*30)
df = pd.DataFrame(data=d, dtype=np.int8)
print(df.dtypes)
print('-'*30)
df2 = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]) ,columns=['a','b','c'])
print(df2)
print('-'*30)
data = np.array([(1,2,3),(4,5,6),(7,8,9)], dtype=[("a","i4"),("b","i4"),("c","i4")])
df3 = pd.DataFrame(data, columns=['c','a'])
print(df3)