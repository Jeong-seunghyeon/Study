import pandas as pd

dat01 = pd.read_csv('./_dataSetPandas/concat_1.csv')
print(dat01)

file_path = './_dataSetPandas/read_csv_sample.csv'

df1 = pd.read_csv(file_path)
print(df1,'\n')
print(type(df1))