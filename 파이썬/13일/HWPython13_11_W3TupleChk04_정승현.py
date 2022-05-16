#HWPython13_11_W3TupleChk04_정승현.py


#연습 01(Unpack)
a = ('apple','banana','cherry')
(green,yellow,red) = a
print(green)
print(yellow)
print(red)
print('-'*15)



#연습 02 (Asterisk01)
a = ('apple','banana','mango','cherry')
(green,yellow,*red) = a
print(green)
print(yellow)
print(red)


print('-'*15)

#연습 03 (Asterisk02)

a = ('apple','banana','mango','cherry')
(green,*tropic,red) = a
print(green)
print(tropic)
print(red)

print('-'*15)