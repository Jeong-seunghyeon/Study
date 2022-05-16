import pandas as pd


df1 = pd.read_excel('./_dataSetPandas/datalabPractice01.xlsx',engine='openpyxl')

df2 = pd.read_excel('./_dataSetPandas/datalabPractice01.xlsx', \
    sheet_name='Sheet1', usecols=[0,1], skiprows=[0,2,3,5], \
    skipfooter=1, header=None, engine='openpyxl')

print(df2.columns,'\n')
print(df2,'\n')
print(df1.columns)



