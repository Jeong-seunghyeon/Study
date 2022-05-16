import pandas as pd

gapminder = pd.read_csv('./_dataSetPandas/gapminder.tsv',sep='\t')

print(len(gapminder))           # 자료 크기
print(type(gapminder))          # 타입
print(gapminder.shape)          # 차원
print(gapminder.columns)        # 컬럼