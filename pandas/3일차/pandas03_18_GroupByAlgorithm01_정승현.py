import pandas as pd
import numpy as np

gapminder = pd.read_csv('../_dataSetPandas/gapminder.tsv',sep='\t')


    
uniList = gapminder['year'].unique()
uniYear = []
for x in uniList:
    uniYear.append(x)
    #print(x)
    if int(x) == 1952:
        gr1952 = gapminder[gapminder['year'] == x]

for y in range(len(uniYear)):
    if uniList[y] == uniYear[y]:
        grYear = gapminder[gapminder['year'] == uniYear[y]]
        print(f"{uniYear[y]}년 {len(grYear)}개 데이터")
        print(f"{uniYear[y]}년 평균 기대수명 : {sum(grYear['lifeExp'])/len(grYear)}")
        
# print(f"1952년 {len(gr1952)}개 데이터")
# print(f"1952년 평균 기대수명 : {sum(gr1952['lifeExp'])/len(gr1952)}")

    
