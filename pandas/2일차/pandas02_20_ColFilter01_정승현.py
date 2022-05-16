import pandas as pd

df = pd.read_csv('./_dataSetPandas/gapminder.tsv',sep='\t')
print(df.head(3))

country_df = df['country']

print(type(country_df))

country_df.head(3)

print(country_df.tail())

subset = df[['country','continent','year']]

print(type(subset))

print(subset.head())

print(subset.tail())