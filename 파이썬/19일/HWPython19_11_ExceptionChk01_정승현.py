#HWPython19_11_ExceptionChk01_정승현.py

#1 ZeroDivisionError
print(100/0)

#2 KeyError
thisdict = {
'brand':'ford',
'model':'mustang',
'year':1964
}

x = thisdict['color']
print(x)

#3 Name Error
print(x)


#4 Type Error
print(10+'50')

#5 fileNotFoundError

f=open('acbd.txt','r')


