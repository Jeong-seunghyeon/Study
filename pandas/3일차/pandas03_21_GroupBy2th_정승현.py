import pandas as pd
import numpy as np

gapminder = pd.read_csv('../_dataSetPandas/gapminder.tsv',sep='\t')


uni = gapminder.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean()

print(uni)
