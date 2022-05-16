
word = ['winter', 'cold', 'positive', 'negative', 'positive']
a = set(word)
print(a)

wordDic = {}

for i in a:
	wordDic[i] = word.count(i)
print(wordDic)

for i in wordDic:
	print(i,'단어의 갯수는 ', wordDic[i],'개 입니다.')
print()
print()
for x in a:
	print(x,'단어 개수는 :',word.count(x),'개 입니다.')
