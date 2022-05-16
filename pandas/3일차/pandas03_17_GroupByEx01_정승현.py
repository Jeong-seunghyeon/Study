import pandas as pd
import numpy as np

gapminder = pd.read_csv('../_dataSetPandas/gapminder.tsv',sep='\t')

print(f"02. {'='*50}")

Uni = gapminder['year'].unique()
nUni = gapminder['year'].nunique()

print(f"^ gapminder['year'] 중복 확인 !!")
print(type(Uni))

print(Uni)
print(nUni)

print(f"03. {'='*50}")

print(gapminder.groupby('year'))
print(gapminder.groupby('year')['lifeExp'])
print(gapminder.groupby('year')['lifeExp'].mean())
print(gapminder['year'].unique())