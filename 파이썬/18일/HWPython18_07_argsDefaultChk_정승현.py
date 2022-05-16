#HWPython18_07_argsDefaultChk_정승현.py


def say_myself(name,old,man=True):
	print('나의 이름은 %s 입니다.'%name)
	print('나이는 %d 입니다.'%old)

	if man:
		print('남자입니다.')
	else:
		print('여자입니다.')

say_myself('소나무',27)
print()

say_myself('오렌지',27,False)
print()
