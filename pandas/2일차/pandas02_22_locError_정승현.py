import pandas as pd

df = pd.read_csv('./_dataSetPandas/gapminder.tsv',sep='\t')

print(df.head(3))

print(df.iloc[-1])
print(df.tail())
print(len(df))