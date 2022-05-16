#HWPython16_01_dictEx01_정승현.py



'''
01. key:value pairs, curly brackets,
02. 3.7 dictionaries are ordered , 3.6 and earlier, dictionaries are unordered.
'''

#연습 01
a = {
	"brand" : "forshe",
	"model" : "boxter",
	"year" : "2020"
}
print(a)
print('-'*30)

# 연습 02
a = {
	"brand" : "forshe",
	"model" : "boxter",
	"year" : "2020"
}
print('-'*30)
print(a["brand"])



#연습 03
a = {
	"brand" : "forshe",
	"model" : "boxter",
	"year" : "2020",
	"year" : "2019"
}

print(a)
print('-'*30)


#연습 04

a = {
	"brand" : "forshe",
	"model" : "boxter",
	"year" : "2020",
	"year" : "2019"
}
print(len(a))
print('-'*30)

#연습 05
a = {
	"brand" : "forshe",
	'electric' : False,
	'year' : 1999,
	'color' : ['red','blue','yellow']
	}
print(a)
print('-'*30)

#연습 06
a = {
	"brand" : "forshe",
	'electric' : False,
	'year' : 1999,
	'color' : ['red','blue','yellow']
}
print(type(a))
print('-'*30)