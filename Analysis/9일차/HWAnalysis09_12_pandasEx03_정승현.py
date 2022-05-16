import pandas as pd
import numpy as np

df = pd.DataFrame([[1,2],[4,5],[7,8]], index=['cobra','viper','sidewinder'], columns=['max_speed','shield'])

#print(df.loc['cobra':'viper','max_speed'])

#print(df.loc[pd.Series([False,True,False],index=['viper','sidewinder','cobra'])])

print(df.loc[pd.Index(["cobra","viper"],name='foo')])