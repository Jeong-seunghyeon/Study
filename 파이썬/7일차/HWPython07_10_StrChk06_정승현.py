#HWPython07_10_StrChk06_정승현.py




a = "Life is too short, You need Python"
c = "123456|        |          |       "
b = a[0] + a[1] + a[2] + a[3]
print(b)





print(a[0:4])                                     #Life
    
print(a[0:2], a[5:7], a[12:18])                   #Li, is, short,
print(a[19:])                                     #You need Python
print(a[:5])                                      #Life 
print(a[:])                                       #Life is too short, You need Python
print(a[19:-7])                                   #You need 