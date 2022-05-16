import csv
#-------------------------------------------------------------------
temperRegionFileList = ['_seoulNullChk.csv', '_daejeonNullChk.csv', '_daeguNullChk.csv', '_busanNullChk.csv', '_gwangjuNullChk.csv']


# MenuSetting01 : 배열에 기술된 파일의 첫행만 추출한다. ==============

temperFirstLine = []
temperRegionDic={}
regionName=[]
regionNum=[]
regionMenu = []
temperatureFileList=[]
a1 = []
a2 = []
a3 = []

for city in temperRegionFileList:
    file=open('./_dataSetGilBut01/temperRegionChk.csv','r', encoding='949')
    file=csv.reader(file)
    vHeader=next(file)
    temperFirstLine.append(vHeader)
# print(temperFirstLine)

file=open('./_dataSetGilBut01/temperRegionChk.csv','r', encoding='949') 
temperRegionFile=csv.reader(file)
temperRegionDic=dict(temperRegionFile)

# print(temperRegionDic)

with open('./_dataSetGilBut01/temperRegionChk.csv','r', encoding='949') as rData:
	rData = csv.reader(rData)
	mydict = {rows[0]:rows[1] for rows in rData}
	a1.append(mydict)
	for x in a1:
		a2.append(x.values())
		for y in x:
			a3.append(y)
	for z in a2:
		Menu = list(z)

for dic in temperRegionDic:
	regionNum.append(dic)
	for x in  range(len(temperFirstLine)):
		if dic.split(":")[0]==temperFirstLine[x][1]:
			regionName.append(temperRegionDic[dic])
			regionNum.append(temperFirstLine[x][1])
for firstLine in temperFirstLine:
	if firstLine[1] in temperRegionDic.keys():
		regionName.append(temperRegionDic[firstLine[1]])
		regionNum.append(firstLine[1])
		regionMenu.append("6:종료")





for x in range(len(regionNum)):
	regionName.append(Menu[x])
	regionMenu.append(Menu[x] + ':' + regionNum[x])


#------regionTitle
def regionTitle():
    print(f'{" 기온 공공데이터 분석 프로젝트 Ver01. ":=^80}')
    print()
    for i in range(len(regionMenu)):
        vmenu=regionMenu[i].split(",")
        print(vmenu, end="   ")
    print()
    print()
    print("="*93)
    print()


#--subMenuTitle---------------------------------------
def subMenuTitle():
    city=""
    userInput=input("\t\t메뉴의 번호를 입력하세요 [Q: 메뉴종료]:")
    if userInput.upper()=="Q":
        exit()
    for idx in range(len(regionNum)):
        if userInput==regionNum[idx]:
            idxChk=idx
            city=regionName[idxChk]
            print()
            print(f"\t\t^{city} 지역이 선택 되었습니다.")
            print()
            break
    else:
        print(f"{userInput} >> 해당 지역 없습니다.")
    return city
    

  
#subMenuChk-----------------------------------------------
def subMenuChk(city):
	
	if city in regionName:
		# print(regionName.index(city))
		idx=regionName.index(city)
		print("-"*25, end="")
		print(f"{city}지역 데이터 개수[{regionDbSet(idx)}]", end="")
		print("-"*25)
		print()
		print("1. 데이터 확인  2.최고/최저 기온  3.월 최고/최저 기온  4.30도 이상  5. -10도 이하  6.날짜범위")
		print("-"*77)
		print()

		while True:
			userInput=input("서브메뉴 번호를 입력하세요 [Q: 서브메뉴 종료]:")
			if userInput=="1":
				print()
				regionPagingData()
			elif userInput=="2":
				print()
				totalMaxMinChk()
			elif userInput=="3":
				monthMaxMinChk()
			elif userInput == '4':
				print('30도 이상 Algorithm Chk')
			elif userInput == '5':
				print('-10도 이하 Algorithm Chk')
			elif userInput=="6":
				dataBetWeenChk()
			elif userInput.upper()== "Q":
				print("서브메뉴를 종료합니다")
				break
			else:
				print()
				print("해당없음")

def getTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

#regionDbSet(idx)-------------------------------------------
def regionDbSet(idx):
    temperatureFileList.clear()
    file=open('./_dataSetGilBut01/temperRegionChk.csv','r', encoding='949') 
    file=csv.reader(file)
    
    for i in file:
        temperatureFileList.append(i)


    return len(temperatureFileList)
    
def regionPagingData():

    dataPerPage=int(input("한 페이지당 출력할 레코드 수를 입력하세요:"))
    totalPage=getTotalPage(len(temperatureFileList), dataPerPage)

    print("-"*50)
    print(f"기온 공공데이터 개수{len(temperatureFileList)}")
    print(f"기온 공공데이터 페이지 개수: {totalPage}")
    print("-"*50)
    # ---------------------------------------------------------------------------------------------
    Page=0
    tempPage=1
    while True:
        print(f"Enter를 치면 다음 {tempPage}/{totalPage} 페이지 {dataPerPage}개 레코드 확인") 
        nowPage=input("확인할 페이지를 입력 또는 Enter[Q:종료]:")
        if nowPage.upper()=="Q":
            print("종료합니다.")
            break
        elif nowPage=="":
            tempPage+=1
            if tempPage==totalPage:
                print("마지막 페이지입니다.")
            else:
                
                for dataOfBeginPage in range(Page,(Page+dataPerPage)):
                    print(f"{dataOfBeginPage}/{len(temperatureFileList)}  {dataOfBeginPage}번째 {temperatureFileList[dataOfBeginPage]}")
                    Page+=1
                print("-"*50)
        else:
            dataOfBeginPage=(int(nowPage)-1)*dataPerPage
            for dataOfBeginPage in range((dataOfBeginPage),(dataOfBeginPage+dataPerPage)):
                if dataOfBeginPage > len(temperatureFileList)-1:
                    print()
                    print("확인할 수 있는 페이지 초과입니다")
                    break
                else:
                    print(f"{dataOfBeginPage}/{len(temperatureFileList)}  {dataOfBeginPage}번째 {temperatureFileList[dataOfBeginPage]}")
                    tempPage=int(nowPage)
#--------------------------------------------------------

def totalMaxMinChk():
	dateMax=-999
	dateMin=999
	print(temperatureFileList)
	for i in temperatureFileList:
		print(i)
		if dateMax < float(i[4]):
			dateMax=float(i[4])
			hotDay=i
		if dateMin > float(i[3]):
			dateMin=float(i[3])
			coldDay=i
	print(f"\t 기상관측 이래 {city}의 최저 기온은 {coldDay[0]}로 {coldDay[3]} 입니다.")
	print(f"\t 기상관측 이래 {city}의 최고 기온은 {hotDay[0]}로 {hotDay[4]} 입니다.")
	
#-----------------------------------------------------------------------------------------------
def dataBetWeenChk():
    print()
    startDate=input("\t\t시작년도:")
    print()
    endDate=input("\t\t종료년도:")
    print()
    for i in temperatureFileList:
        if startDate==i[0]:
            startD=temperatureFileList.index(i)
        if endDate==i[0]:
            endD=temperatureFileList.index(i)
    
    temp=temperatureFileList[startD:endD]
    # print(temp)
    dateMax=-9999
    dateMin=9999
    for i in temp:
        if dateMax < float(i[4]):
            dateMax=float(i[4])
            hotDay=i
        if dateMin > float(i[3]):
            dateMin=float(i[3])
            coldDay=i
    print(f"\t 기상관측 이래 {city}의 [{startDate} ~ {endDate}]")
    print(f"\t 최저 기온은 {coldDay[0]}로 {coldDay[3]} 입니다.")
    print(f"\t 최고 기온은 {hotDay[0]}로 {hotDay[4]} 입니다.")
      

def monthMaxMinChk():
    vMonth=["01","02","03","04","05","06","07","08","09","10","11","12"]
    monthMaxData=[]
    monthMinData=[]
    for monthIdx in vMonth:
        dateMax=-9999
        dateMin=9999
        for i in temperatureFileList:
            if i[0][5:7]==monthIdx:
                if dateMax < float(i[4]):
                    dateMax=float(i[4])
                    hotMonth=i
                if dateMin > float(i[3]):
                    dateMin=float(i[3])
                    coldMonth=i
        monthMaxData.append(hotMonth)
        monthMinData.append(coldMonth)
    for idx in range(12):
        print(f"기상관측 아래 {city}의 {idx+1}월 최고 기온은 {monthMaxData[idx][0]}으로 {monthMaxData[idx][4]}도 입니다")
        print(f"기상관측 아래 {city}의 {idx+1}월 최저 기온은 {monthMinData[idx][0]}으로 {monthMinData[idx][3]}도 입니다")
        print()


while True:
    regionTitle()
  
    city=subMenuTitle()
  
    subMenuChk(city)