#HWPython17_02_StudentMS_V01_Step01_정승현.py
# 함수 stuTitle()


menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0;




def stuTitle():
	print('-'*100)
	print(' >> 학생관리시스템v01 <<')
	print('-'*100)
	print('  '.join(menu))
	print('-'*100)
	
		

while True:
	stuTitle()
	num = int(input('번호 입력 : '))
	if num == 1:
		print('1. 탈퇴학생		Algorithm Chk')
	elif num == 2:
		print('2. 추가등록		Algorithm Chk')
	elif num == 3:
		print('3. 학생목록		Algorithm Chk')
	elif num == 4:
		print('4. 합격생목록		Algorithm Chk')
	elif num == 9:
		print('9. 메뉴종료')
		exit()
	else:
		print('입력한 번호를 확인해 주세요.')
		
