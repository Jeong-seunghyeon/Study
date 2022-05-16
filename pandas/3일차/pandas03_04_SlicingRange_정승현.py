import pandas as pd
import numpy as np

gapminder = pd.read_csv('../_dataSetPandas/gapminder.tsv',sep='\t')

small_range = list(range(5))

print(gapminder.head(3))
print()

subset = gapminder.iloc[:,small_range]
print(subset.head())

small_range = list(range(3,6))

subset = gapminder.iloc[:,small_range]
print(subset.head())

small_range = list(range(0,6,2))
subset = gapminder.iloc[:,small_range]
print(subset.head())