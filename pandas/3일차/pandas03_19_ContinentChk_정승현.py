import pandas as pd
import numpy as np

gapminder = pd.read_csv('../_dataSetPandas/gapminder.tsv',sep='\t')

UniList = gapminder['continent'].unique()
uniYear = gapminder['year'].unique()
UniCont = []

print(f"대륙의 종류 : {UniList} 갯수 : {len(UniList)}")

for idx in range(len(uniYear)):
    if uniYear[idx] == uniYear[idx]:
        grYear = gapminder[gapminder['year'] == uniYear[idx]]
for x in UniList:
    UniCont.append(x)

for y in range(len(UniList)):
    if UniList[y] == UniCont[y]:
        grCont = gapminder[gapminder['continent'] == UniCont[y]]
        print(f"{UniCont[y]} 대륙 {len(grCont['country'].unique())}개 국가")
        print(f"{UniCont[y]}대륙 : {grCont['country'].unique()}")
        for z in range(len(uniYear)):
            vIdx = grCont[grCont['year']==uniYear[z]]
            #print(vIdx[['continent','lifeExp']])
            print(f"{UniCont[y]}대륙 {uniYear[z]}년 평균기대 수명 : {(sum(vIdx['lifeExp'])/len(vIdx['lifeExp']))}")
        
        
