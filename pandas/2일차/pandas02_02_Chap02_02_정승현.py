import pandas as pd

file_path = './_dataSetPandas/read_csv_sample.csv'

df1 = pd.read_csv(file_path)
print(df1, '\n')

df2 = pd.read_csv(file_path,header=None)
print(df2,'\n')

df3 = pd.read_csv(file_path,index_col=None)
print(df3,'\n')

df4 = pd.read_csv(file_path,index_col='c0')
print(df4,'\n')