#HWPthon07_17_StrExam01_정승현.py


a = 'https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=html&qdt=0&ie=utf8&query=html'
b = a.split('?')
print("URL : "+b[0])

c = b[1].split('&')






for Query in c:
	print("Query String : "+ (Query))

print(len(c))
	



