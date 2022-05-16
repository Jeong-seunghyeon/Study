import pandas as pd
import numpy as np

gapminder = pd.read_csv('../_dataSetPandas/gapminder.tsv',sep='\t')


print(gapminder.iloc[0:3])


print(gapminder.loc[0:2][['year','pop']])


print(gapminder.loc[0:2,['year','pop']])
print(gapminder.iloc[0:3,[2,4]])
