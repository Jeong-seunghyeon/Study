import pandas as pd

df = pd.read_csv('./_dataSetPandas/gapminder.tsv',sep='\t')

print(df.shape, df.shape[1])
number_of_rows = df.shape[0]

print(number_of_rows,'\n\n')

last_row_index = number_of_rows -1

print(df.loc[last_row_index])
print(df.loc[len(df)-1])
print(df.tail(n=1))
print(df.tail(n=2))
print(df.loc[[0,99,999]])