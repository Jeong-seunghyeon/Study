#HWPython14_03_DoitSetEx03_정승현.py


# 값 1개 추가하기(add) 항목

s1 = set([1,2,3])
s1.add(4)
print(s1)
print('-'*20)

# 값 여러 개 추가하기 (update)_Iterable (중복 불가)
s1 = set([1,2,3])
s1.update([4,5,6,3,6])
print(s1)
print('-'*20)


# 특정값 제거하기(remove)_항목
s1 = set([1,2,3])
s1.remove(2)
print(s1)

