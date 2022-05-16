import pandas as pd

url='./_dataSetPandas/Test01.html'

tables = pd.read_html(url)

print(tables)

print(len(tables),'\n==>')

for i in range(len(tables)):
    print("tables[%s]" %i, '\n')
    print(tables[i], '\n')

df = tables[1]
print(df.columns,'\n')