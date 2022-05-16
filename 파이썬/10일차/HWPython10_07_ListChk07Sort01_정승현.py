#HWPython10_07_ListChk07Sort01_정승현.py

#연습 01 (acending, by default)
a = ['apple','banana','cherry','mango','kiwi']
a.sort()
print(a)




# 연습 02 (numerically)
a = [100,50,65,82,23]
a.sort()
print(a)


#연습 03 (reverse = True)
a = ['apple','banana','cherry','mango','kiwi']
a.sort(reverse = True)
print(a)




#연습 04 (reverse = True)
a = [100,50,65,82,23]
a.sort(reverse = True)
print(a)




#연습 05 (Function)
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)