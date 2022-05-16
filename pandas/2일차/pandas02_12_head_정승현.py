import pandas as pd

df = pd.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion',
                   'monkey', 'parrot', 'shark', 'whale', 'zebra']})

print(df,'\n==>')
print(df.head(),'\n==>')

print(df.head(3),'\n==>')
print(df.head(-3),'\n==>')

