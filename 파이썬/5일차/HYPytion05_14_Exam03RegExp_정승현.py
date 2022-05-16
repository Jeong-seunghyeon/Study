#HYPytion05_14_Exam03RegExp_정승현.py
## 참인경우 if 거짓인경우



grade = [90, 30, 60, 50, 80]


for idx in range(len(grade)):
	jumsu = grade[idx]
	print(f'{idx+1}번 학생 {jumsu}점 합 격' if jumsu >=60 else f'{idx+1}번 학생 {jumsu}점 불합격')



grade = [90, 30, 60, 50, 80]

for idx in range(len(grade)):
	result="합격"if grade[idx] >= 60 else "불합격"

	print("%d번 학생 %3d점 %3s 입니다." %(idx+1, grade[idx], result))


	







grade= [90,30,60,50,80]

for idx in range(len(grade)):
	jumsu = grade[idx]
	print(f'{idx+1}번 학생 {jumsu}점 합 격' if jumsu >= 60 else f'{idx+1}번 학생 {jumsu}점 불합격')



for idx in range(len(grade)):
	result="합격"if grade[idx] >= 60 else"불합격"
	print("%d번 학생 %3d점 %3s 입니다." %(idx+1, grade[idx], result))

