import csv

regionName = []
regionNum = []
regionMenu = []
vMenu = ['서울 : 108', '대전 : 133', '대구 : 143', '부산 : 159', '광주 : 156', '울산 : 152', 'Q : 종료']
temperRegionFileList = ['seoulNullChk.csv', 'daejeonNullChk.csv', 'daeguNullChk.csv', 
        'busanNullChk.csv', 'gwangjuNullChk.csv', 'ulsanNullChk.csv']
temperFirstLine = []
mydict = {}
a1 = []
a2 = []
a3 = []


with open('./_dataSetGilBut01/temperRegionChk.csv','r', encoding='949') as rData:
	rData = csv.reader(rData)
	mydict = {rows[0]:rows[1] for rows in rData}
	a1.append(mydict)
	for x in a1:
		a2.append(x.values())
		for y in x:
			a3.append(y)
	for z in a2:
		menu = (list(z))

for firstLine in vMenu:
	if firstLine[5:] in mydict.keys():
		regionMenu.append(firstLine[:2]+':'+firstLine[5:])
		regionNum.append(firstLine[5:])
		regionName.append(firstLine[:2])
	
print(menu)
#------------------------------------타이틀------------------------------------------------------------------------------
def regionTitle():
	print('='*40,'기온 공공데이터 분석 프로젝트 Ver01.','='*40)
	print(regionMenu)
	print('='*118)

#-------------------------------------메뉴선택-----------------------------------------------------
def menuList():
	print('='*50,'메뉴선택','='*50)
	print()
	for m in regionMenu:
		print(m,end=' ')
	print('\n')
	print('='*110)
	print()
#--------------------------------------메뉴 입력 ----------------------------------------------------



def subMenuChk():
	while True:
		print(regionMenu)
		print()
		a = input('메뉴의 번호를 선택해 주세요 [ Q : 메뉴종료 ] : ')
		print()
		aChk = 0
		if a.upper() == 'Q':
			print('종료합니다.')
			exit()
		else:
			for idx in range(len(regionNum)):
				if a == regionNum[idx]:
					aChk = 1
					region = regionName[idx]
			if aChk == 1:
				print(region,'지역을 선택했습니다.')
				subMenuTitle()
			else:
				print('입력하신 번호를 확인하세요')



#--------------------------------------특정 행 출력----------------------------------------------------
def printFirst():
	n = int(input('출력하실 행 번호를 입력하세요'))
	for x in temperRegionFileList:
		f = open('./_dataSetGilBut01/'+x,'r', encoding='949')
		data = csv.reader(f)
		data1 = list(data)
		temperFirstLine.append(data1[n])
	print(temperFirstLine)
#---------------------------------하위메뉴-------------------------------------------------------------
def subMenuTitle():
	while True:
		print('='*40,'기온 공공데이터 분석 프로젝트 Ver01.','='*40)
		print('1. 데이터 확인    2. 최고/최저 기온    3. MenuChk    4.30도이상    5.MenuChk    6.MenuChk')
		print('='*118)
		
		Num = input('메뉴의 번호를 선택해주세요 [ Q : 메뉴종료 ] : ' )
		if Num == '1':
			print()
			print('데이터 확인')
			print()
		elif Num == '2':
			print()
			print('최고/최저 기온 확인')
			print()
		elif Num == '3':
			print()
			print('MenuChk')
			print()
		elif Num == '4':
			print()
			print('월별 영상 30도 이상 Chk ! ')
			print()
		elif Num == '5':
			print()
			print('MenuChk')
			print()
		elif Num == '6':
			print()
			print('MenuChk')
			print()
		elif Num.upper() == 'Q':
			print()
			print('돌아갑니다..')
			regionTitle()
			break
		else:
			print('입력하신 번호를 확인하세요.')
#------------------------------------------실행-------------------------------------------------------------------
regionTitle()
subMenuChk()

