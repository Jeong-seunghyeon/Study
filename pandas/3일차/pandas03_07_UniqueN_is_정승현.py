import pandas as pd
import numpy as np

gapminder = pd.read_csv('../_dataSetPandas/gapminder.tsv',sep='\t')

result = pd.Series([2,1,3,3]).unique()

print(result)


s = pd.Series([1,3,5,7,7])
print(s.nunique())

s = pd.Series([1,3,5,7])

print(s.is_unique)