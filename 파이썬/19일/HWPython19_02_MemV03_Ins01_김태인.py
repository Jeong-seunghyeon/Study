menu    = ['1.회원가입', '2.로그인', '3.회원목록','4.정보수정','5.회원탈퇴', '9.메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = []
userList=[]
temp=[]
loginInfo=[]

for menu2 in range(len(menu)):
	menuChk.append(menu[menu2][0])
print(menuChk)


#메뉴타이틀-------------------------------------------------------------------------------------
def menuList():
	print("="*27,"메뉴선택","="*27)
	print()
	for m in menu:
		print(m, end=" ")
	print("\n")
	print("="*64)
	print()

#메뉴선택-------------------------------------------------------------------------------------
def menuSelect():
	num=0
	num=input("\t""메뉴의 번호를 입력해주세요 :")
	if num in menuChk:
		return num
	else:
		print("\t""다시 입력해주세요")
		print()

#1번-------------------------------------------------------------------------------------------
def memIns():
	temp=[]	
	print("\t\t","^SignUp !")
	print()
	for signUp in itemList:
		print(f"\t{signUp:<10}:",end="") 
		templist=input()
		temp.append(templist)
	userList.append(temp)
	f=open("MemV03.txt","w")
	for i in range(len(userList)):
		a=","
		b= "\n"
		for x in range(len(userList[i])):
			data="%s"%userList[i][x]
			f.write(data)
			if x < len(userList[i])-1:
				f.write(a)
		f.write(b)
	
	for vList in userList:
		print(vList)
	print(f"현재 회원수는 {len(userList)}명입니다")	
	print()
		
	

#2번-------------------------------------------------------------------------------------------
def memLog():
	temp=[]
	if len(userList)==0:
		print()
		print("{0:>25}".format("먼저 회원가입해주세요"))
		print()
	else:
		print("\t\t","^Log in !")
		print()
		print()
		for signIn in range(2):
			print(f"\t{itemList[signIn]}:",end="")
			templist=input()
			temp.append(templist)
		chkMem=0
		for idx in range(len(userList)):
			if temp[0] == userList[idx][0]:
				chkMem=1
				break
		if chkMem==1:
			if temp[1]==userList[idx][1]:
				print("{0:>25}".format("로그인 성공"))
				print()
				print()
			elif userList[idx][1]!=temp[1]:
				print("{0:>25}".format("비번확인"))
				print()
				print()
		elif temp[0] != userList[idx][0]:
			print("{0:>25}".format("아이디 확인"))
			print()
			print()
	

#3번-------------------------------------------------------------------------------------------
def memList():
	print("\t\t","^Member List !")
	if len(userList)==0:
		print()
		print("{0:>25}".format("먼저 회원가입해주세요"))
		print()
	else:
		print('='*50)
		for a in itemList:
			print("{0:^7}".format(a), end='')
		print()
		print('='*50)
		print()
		for x in userList:
			for y in x:
				print("{0:^7}".format(y), end='')
			print()
	print()

#9번-------------------------------------------------------------------------------------------
def memExit():
	print("\t""9. 메뉴를 종료합니다")
	print()

#4번-------------------------------------------------------------------------------------------
def memUpd():
	temp=[]
	if len(userList)==0:
		print()
		print("{0:>25}".format("먼저 회원가입해주세요"))
		print()
	else:
		print("\t\t","^회원 정보 수정")
		print()
		print()
		for signIn in range(2):
			print(f"\t{itemList[signIn]}:",end="")
			templist=input()
			temp.append(templist)
		chkMem=0
		for idx in range(len(userList)):
			if temp[0] == userList[idx][0]:
				chkMem=1
				break
		if chkMem==1:
			if temp[1]==userList[idx][1]:
				print()
				print()
				print(f"\t\t{temp[0]}님 회원 수정 가능한 상태 입니다.")
				print()
				print("\t", '수정 전 내용',userList[idx])
				print()
				for memUp in range(len(itemList)):
					print(f"\t{itemList[memUp+1]:>10} 바꾸시겠습니까?(Y/N):",end="") 
					answer=input().lower()
					if answer == "y":
						for newInfo in range(1,len(itemList)):
							print(f"\t바꿀{itemList[newInfo]} 입력:",end="") 
							answer2=input()
							(userList[idx][idx+1])=answer2
							print(userList[idx]) 
							break
							
			elif userList[idx][1]!=temp[1]:
				print("{0:>25}".format("비번확인"))
				print()
				print()
		elif temp[0] != userList[idx][0]:
			print("{0:>25}".format("아이디 확인"))
			print()
			print()
		

#5번--------------------------------------------------------------------------------------------
def memDel():
	temp=[]
	if len(userList)==0:
		print()
		print("{0:>25}".format("먼저 회원가입해주세요"))
		print()
	else:
		print("\t\t","^회원탈퇴")
		print()
		print()
		for signIn in range(2):
			print(f"\t{itemList[signIn]} :",end="")
			templist=input()
			temp.append(templist)
		chkMem=0
		for idx in range(len(userList)):
			if temp[0] == userList[idx][0]:
				chkMem=1
				break
		if chkMem==1:
			if temp[1]==userList[idx][1]:
				print("{0:>25}".format("탈퇴 성공"))
				del userList[idx]
				
				print()
				print()
			elif userList[idx][1]!=temp[1]:
				print("{0:>25}".format("비번확인"))
				print()
				print()
		elif temp[0] != userList[idx][0]:
			print("{0:>25}".format("아이디 확인"))
			print()
			print()
		
#메뉴타이틀 반복-------------------------------------------------------------------------------
while True:
	menuList()
	num=menuSelect()

#1번입력-------------------------------------------------------------------------------------
	if num=="1":
		memIns()

#2번입력-------------------------------------------------------------------------------------
	elif num=="2":
		memLog()

#3번입력-------------------------------------------------------------------------------------
	elif num=="3":
		memList()
#4번입력-------------------------------------------------------------------------------------
	elif num=="4":
		memUpd()
		
#5번입력-------------------------------------------------------------------------------------
	elif num=="5":
		memDel()
		
#9번입력-------------------------------------------------------------------------------------
	elif num=="9":
		memExit()
		break

