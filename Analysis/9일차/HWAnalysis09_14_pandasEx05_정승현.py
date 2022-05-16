import pandas as pd
import numpy as np

# df = pd.DataFrame([[1,2],[4,5],[7,8]], index=['cobra','viper','sidewinder'], columns=['max_speed','shield'])

# df.loc[['viper','sidewinder'],['shield']]=50
# print(df)


# df.loc['cobra']=10
# print(df)

# df.loc[:,'max_speed']=30
# print(df)

# df.loc[df['shield']>4]=0
# print(df)

df = pd.DataFrame([[1,2],[4,5],[7,8]],index=[7,8,9],columns=['max_speed','shield'])
print(df)

result = df.loc[7:9]
print(result)