import pandas as pd
import numpy as np

df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
})
# nan = not a number (number가 아니다 Null값 같은 쓰임)

print(df)
print('-'*50)
# print(df.sort_values(by=['col1']))
# print('-'*50)
# print(df.sort_values(by=['col1','col2']))
# print('-'*50)
# print(df.sort_values(by='col1',ascending=False))
# print('-'*50)
# print(df.sort_values(by='col1',ascending=False, na_position='first'))
print(df.sort_values(by='col4', key=lambda col:col.str.lower()))



