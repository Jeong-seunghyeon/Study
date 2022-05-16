import pandas as pd

df = pd.read_json('./_dataSetPandas/read_json_sample.json')
print(df,'\n')
print(df.index)