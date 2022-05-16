#HWPython16_04_dictEx04_정승현.py


#연습 01 key
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
	print(x)
print('-'*50)





#연습 02 key 값을 이용해서 values 가저오기

for x in thisdict:
	print(thisdict[x])
print('-'*50)



#연습 03 2번을 values() 이용해서 가져오기
for x in thisdict.values():
	print(x)
print('-'*50)



#연습 04 1번을 keys() 이용해서 가저오기
for x in thisdict.keys():
	print(x)
print('-'*50)


#연습 05 items() 이용해서 쌍으로 가져오기
for x, y in thisdict.items():
	print(x,':',y)
print('-'*50)



#연습 01 copy() 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

dict1 = thisdict
thisdict.update({"color" : "white"})
print(thisdict)
print(dict1)

print('-'*50)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
mydict.update({"color" : "white"})
print(mydict)
print(thisdict)
print('-'*50)


#연습 02 생성자_dict()

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)