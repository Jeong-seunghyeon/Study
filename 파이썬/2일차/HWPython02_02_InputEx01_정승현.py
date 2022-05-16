vid='orange'
vpwd='1234'

id = input("id를 입력 하세요 :")
pwd = input("Pwd를 입력 하세요 ")


if id==vid:
	if pwd==vpwd:
		print("orange님 로그인 성공")
	elif pwd!=vpwd:
		print("패스워드를 확인하세요")
elif id!=vid:
	if pwd==vpwd:
		print("아이디를 확인하세요")
