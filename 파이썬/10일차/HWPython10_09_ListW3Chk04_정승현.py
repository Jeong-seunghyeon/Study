#HWPython10_09_ListW3Chk09CopyWarmUp_정승현.py


'''
Copy Lists
cannot copy a list simply by typing list2 = list1
because : list2 will only a reference to list1

01. result = list([1,2,3,])
    result = list([1,2,3,])


02. result02 = result01
'''


a = ['apple','banana','cherry']
b = a.copy()
print(b)


a = ['apple','banana','cherry']
b = list(a)
print(b)
