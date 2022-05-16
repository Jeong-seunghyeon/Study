#HWPython16_09_DoitChap02_03_정승현.py


# 연습 문제 7번
a = ['Life','is','too','short']
result = ' '.join(a)
print(result)




# 연습 문제 8번 
a = (1,2,3)
b = a +(4,)
print(b)


#연습 문제 9번
a = dict()
a
{}
#a[[1]] = 'python' 3번이 오류발생



# 연습 문제 10번
a = {'A':90, 'B':80, 'C':70}
a.pop('B')
print(a)


# 연습 문제 11번
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b = set(a)
c = list(b)
print(c)



# 연습 문제 12번
a = b = [1, 2, 3]
a[1] = 4
print(b)
# a = b 이기 때문에 주소값도 가져온다