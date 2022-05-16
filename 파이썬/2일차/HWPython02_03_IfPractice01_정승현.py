#HWPython032_05_IfpractionAndOr_정승현.py
vid='orange'
vpwd='1234'

id = input("id를 입력 하세요 :")
pwd = input("Pwd를 입력 하세요 ")


if id==vid and pwd==vpwd:
	print("orange님 로그인 성공")
elif id!=vid:
	print("아이디를 확인하세요")
else:
	print("패스워드를 확인하세요")




			
	