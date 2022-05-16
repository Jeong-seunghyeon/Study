#HWPython07_08_StrChk04Format_정승현.py


a = 'hello'
b = 'world'
c= a+b
print(c)

a = 'hello'
b = 'world'
c = a + ' ' + b
print(c)





age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} prices of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))



quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


txt ='we are the so-called \"Vikings\" from the north.'
print(txt)

txt = 'we are the so-called "Vikings" from the north.'
print(txt)
