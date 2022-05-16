#HWPython10_09_ListW3Chk09CopyWarmUp_정승현.py


'''
Copy Lists
cannot copy a list simply by typing list2 = list1
because : list2 will only a reference to list1

01. result = list([1,2,3,])
    result = list([1,2,3,])


02. result02 = result01

결과값은 똑같이 나오지만 값을 받는게 아닌 result01에 저장된 리스트값의 위치를 reference 하는것 이다.
'''


a = ['apple','banana','cherry']
b = ['apple','banana','cherry']
print(a)
print(b)
a[1]='1'
print(a)
print(b)

print('-'*50)


a = ['apple','banana','cherry']
b = a
print(a)
print(b)
b[1] = '1'
a[1]='5'
print(a)
print(b)


