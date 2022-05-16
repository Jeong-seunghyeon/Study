#HWPython16_02_dictEx02_정승현.py



#연습 01
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#x = thisdict["model1"]           #에러발생
print('-'*30)

#연습 02

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model1")
print(x)                                      # None
print('-'*30)

#연습 03 Keys()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)
print('-'*30)




#연습 04 keys list gets updated
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
print('-'*30)



# 연습 05 value()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x)
print('-'*30)



#연습 06  values() updated
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
print('-'*30)



#연습 07 items()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x)
print('-'*30)



#연습 08 items() updated
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

print('-'*30)


#연습 09 add
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
print('-'*30)


#연습 10 Key Exists
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in car:
  print("Yes")