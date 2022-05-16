import pandas as pd
import numpy as np

gapminder = pd.read_csv('../_dataSetPandas/gapminder.tsv',sep='\t')

print(gapminder['country'])



print(gapminder.head(3))

subset = gapminder.iloc[:,:3]
print(subset.head())

subset = gapminder.iloc[:,0:6:2]
print(subset.head())