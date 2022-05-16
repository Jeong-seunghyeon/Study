menu =  [' 1. 학생탈퇴', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ', ' 5. 불합격생목록',' 6. 탈퇴목록',' 9. 메뉴종료 ']
menuChk = []
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]
for x in menu:
	menuChk.append(x[1])
idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
exList = []
# -----------------------------------------------
funList = ['', 'stuDel()', 'stuIns()', 'stuSel()', 'stuPass()', 'stuNonPass()', 'stuDelSel()' ] 
# -----------------------------------------------
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

menuNum = [1,2,3,4,9]

dic = {}
deleteIDList = {}
idx = 0;

def Title():
	print('-'*120)
	print(menu)
	print('-'*120)

def menuSelect():
	num = input('번호를 입력해 주세요. : ')
	if num in menuChk:
		return int(num);


def stuDel():
	print('학생탈퇴 Algorithm Chk')

def stuIns():
	print('stuIns Algorithm Chk')

def stuSel():
	print('stuSel Algorithm Chk')

def stuPass():
	print('stuPass Algorithm Chk')

def stuNonPass():
	print('stuNonPass Algorithm Chk')

def stuDelSel():
	print('stuDelSel Algorithm Chk')

	



while True:
	Title()
	nums = menuSelect()
	if nums in range(0,len(menuChk)):
		eval(funList[nums])
	elif nums == 9:
		print('종료합니다')
		exit()
	else:
		print('입력하신 번호를 확인하세요.')
