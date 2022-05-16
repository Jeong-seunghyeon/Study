list(filter(lambda x: x>0, [1,-3,2,0,-5,6]))

result1 = filter(lambda x : x > 0 , [1,-3,2,0,-5,6])
print(type(result1))
print(list(result1))


result2 = map(lambda a : a*2 , [1,2,3,4])
print(type(result2))
print(list(result2))
