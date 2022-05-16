import pandas as pd
import numpy as np

gapminder = pd.read_csv('../_dataSetPandas/gapminder.tsv',sep='\t')

print(gapminder.shape)

Uni = gapminder['year'].unique()
nUni = gapminder['year'].nunique()
print(type(Uni))

print(Uni)
print(nUni)