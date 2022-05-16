import pandas as pd

df = pd.DataFrame({'Animal':['Falcon','Falcon','Parrot','Parrot'],'Max Speed':[380.,370.,34.,36.]})

print(f"{df}\n{'>'*50}")

result = df.groupby(['Animal'])

print(f"{result}\n{'>'*50}")

result = df.groupby(['Animal']).mean()

print(f"{result}\n{'>'*50}")
print(type(result))