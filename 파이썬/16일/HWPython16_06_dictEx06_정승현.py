#HWPython16_06_dictEx06_정승현.py


#연습 01
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)


#연습 02


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color","red")

print(x)