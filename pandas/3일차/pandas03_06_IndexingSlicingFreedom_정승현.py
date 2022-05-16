import pandas as pd
import numpy as np

gapminder = pd.read_csv('../_dataSetPandas/gapminder.tsv',sep='\t')

print(gapminder.loc[[0,100,1000],['country','lifeExp','gdpPercap']])
print(gapminder.loc[100:111,['country','lifeExp','gdpPercap']])


print(gapminder.iloc[[0,100,1000],[0,3,5]])

print(gapminder.iloc[100:111,[0,3,-1]])