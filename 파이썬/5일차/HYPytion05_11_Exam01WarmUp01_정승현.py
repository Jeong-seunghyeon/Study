#HYPytion05_12_Exam01_정승현.py

'''

grade = [90,30,60,50, 80]

for jumsu in grade:
	print(jumsu)

print(len(grade))

for jumsu in range(len(grade)):
	print(grade)
'''


grade = [90, 30, 60, 50, 80]


for idx in range(len(grade)):
	if grade[idx] >= 60:
		print("%d번 학생 %3d점 %3s입니다." %(idx+1, grade[idx], '합   격'))
	else :
		print("%d번 학생 %3d점 %3s입니다." %(idx+1, grade[idx], '불 합 격'))








