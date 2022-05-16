import pandas as pd

titanic = pd.read_csv('./_dataSetPandas/train.csv')

print(titanic.columns)
print(titanic.index)
print(titanic.head(3))
print(titanic.tail(3))
print(titanic['Survived'])
print(titanic[['PassengerId','Survived']])
print(titanic.iloc[::5])
print(len(titanic),len(titanic.columns))

Atitanic = titanic.sort_values(by=['Age'],ascending=False)

print(Atitanic[['Name','Age','Survived']].head(15))

