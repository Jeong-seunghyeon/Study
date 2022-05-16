import pandas as pd


df2 = pd.read_excel('./_dataSetPandas/datalabPractice01.xlsx',engine='openpyxl')
print(df2)

df1 = pd.read_excel('./_dataSetPandas/datalabPractice01.xlsx',engine='xlrd')

print(df1)

