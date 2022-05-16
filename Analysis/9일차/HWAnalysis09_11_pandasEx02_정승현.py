import pandas as pd
import numpy as np

df = pd.DataFrame([[1,2],[4,5],[7,8]], index=['cobra','viper','sidewinder'], columns=['max_speed','shield'])

print(df)
print('-'*30)

print(df.loc['viper'])
print('-'*30)


print(df.loc[['viper','sidewinder']])
print('-'*30)

print(df.loc['sidewinder','shield'])
print('-'*30)
