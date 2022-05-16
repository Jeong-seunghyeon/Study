import pandas as pd
import numpy as np

gapminder = pd.read_csv('../_dataSetPandas/gapminder.tsv',sep='\t')

print(gapminder.head(2))

subset_loc = gapminder.loc[0]
subset_tail = gapminder.tail(1)
subset_head = gapminder.head(1)

print(f"\n{'-'*15}\n{subset_loc}")
print(f"\n{'-'*15}\n{subset_tail}")
print(f"\n{'-'*15}\n{subset_head}")

print(type(subset_loc))
print(type(subset_tail))
print(type(subset_head))