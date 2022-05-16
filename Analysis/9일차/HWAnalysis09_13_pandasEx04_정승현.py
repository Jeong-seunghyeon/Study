import pandas as pd
import numpy as np

df = pd.DataFrame([[1,2],[4,5],[7,8]], index=['cobra','viper','sidewinder'], columns=['max_speed','shield'])

#print(df.loc[df['shield']>4])

print(df.loc[df['shield']>4, ['max_speed']])

result = df.loc[lambda df: df['shield']==8]

print(result)