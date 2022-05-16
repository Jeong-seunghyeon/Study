#HWPython14_05_W3SetEx02_정승현.py


#01. Cannot access index
#02. in keyword


#연습 01 (for in )
a = {'apple','banana','cherry'}
for x in a:
	print(x)
print('-'*20)


#연습 02 (in)
a = {'apple','banana','cherry'}
print('banana' in a)
print('-'*20)

#연습 01 (add_항목)
a = {'apple','banana','cherry'}
a.add('orange')
print(a)
print('-'*20)


#연습 02 (set_update())
a = {'apple','banana','cherry'}
b = {'grape','mango','kiwi'}
a.update(b)
print(a)
print('-'*20)


#연습 03 (Collection_update())
a = {'apple','banana','cherry'}
b = ['kiwi','grape','mango']
a.update(b)
print(a)
print('-'*20)




#연습 01 (remove()_Error Chk)
a = {'apple','banana','cherry'}
a.remove('banana')
print(a)
print('-'*20)
a = {'apple','banana','cherry'}
#a.remove('orange') 에러 발생
print(a)
print('-'*20)



#연습 02 (discard()_Error Chk)
a = {'apple','banana','cherry'}
a.discard('banana')
print(a)
print('-'*20)

a = {'apple','banana','cherry'}
a.discard('oragne')   #에러 미발생
print(a)
print('-'*20)


#연습 03 (pop())
a = {'apple','banana','cherry'}
x = a.pop()
print(x)
print(a)
print('-'*20)



#연습 04 ( clear())
a = {'apple','banana','cherry'}
a.clear()
print(a)
print('-'*20)                          # 'clear'는 데이터는 삭제되어도 형식은 남아있음


#연습 05 (del 차이점)
a = {'apple','banana','cherry'} 
del a                                  # 'del' 은 데이터도 삭제되고 형식도 사라져서 오류 발생
print(a)
