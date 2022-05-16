import pandas as pd

gapminder = pd.read_csv('./_dataSetPandas/gapminder.tsv',sep='\t')
print(gapminder)
print(type(gapminder))