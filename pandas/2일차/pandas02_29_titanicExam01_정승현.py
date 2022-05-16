import pandas as pd

titanic = pd.read_csv('./_dataSetPandas/train.csv')

print(type(titanic))

print(titanic.columns)