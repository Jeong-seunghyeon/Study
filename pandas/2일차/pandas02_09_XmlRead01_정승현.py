import pandas as pd

url='./_dataSetPandas/Test01.html'

tables = pd.read_html(url)

print(tables)