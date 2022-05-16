import pandas as pd

df = pd.read_csv('./_dataSetPandas/gapminder.tsv',sep='\t')
print(df.head(3))
print(df.shape)
loc00 = df.loc[0]
print(type(loc00))
print(df.loc[90:100])
print(df.loc[99])
print(df.tail(3))