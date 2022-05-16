import pandas as pd

s = pd.Series(['lama','cow','lama','beetle','lama','hippo'],name='animal')

print(s.isin(['cow','lama']))

print(s.isin(['lama']))