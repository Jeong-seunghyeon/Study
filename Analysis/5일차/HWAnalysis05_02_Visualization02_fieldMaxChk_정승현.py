import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
#-------------------------------------------------------------------
temperRegionFileList = ['_seoulNullChk.csv', '_daejeonNullChk.csv', '_daeguNullChk.csv', '_busanNullChk.csv', '_gwangjuNullChk.csv']


# MenuSetting01 : 배열에 기술된 파일의 첫행만 추출한다. ==============

temperFirstLine = []
temperRegionDic={}
regionName=[]
regionNum=[]
regionMenu = []
temperatureFileList=[]




for city in temperRegionFileList:
    file=open(f"_dataSetGilBut01/{city}","r",encoding="cp949")
    file=csv.reader(file)
    vHeader=next(file)
    temperFirstLine.append(vHeader)
print(temperFirstLine)

file=open(f"_dataSetGilBut01/temperRegionChk.csv","r",encoding="cp949")
temperRegionFile=csv.reader(file)
temperRegionDic=dict(temperRegionFile)

# print(temperRegionDic)

for dic in temperRegionDic:
    for x in  range(len(temperFirstLine)):
        if dic.split(":")[0]==temperFirstLine[x][1]:
            regionMenu.append(temperRegionDic[dic]+":"+temperFirstLine[x][1])
            regionName.append(temperRegionDic[dic])
            regionNum.append(temperFirstLine[x][1])
# for firstLine in temperFirstLine:
#   if firstLine[1] in temperRegionDic.keys():
#     regionMenu.append(temperRegionDic[firstLine[1]]+":"+firstLine[1])
#     regionName.append(temperRegionDic[firstLine[1]])
#     regionNum.append(firstLine[1])
regionMenu.append("6:종료")

print(regionMenu)
print(regionName)
print(regionNum)



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
            print(f"\t\t^{regionName[idxChk]} 지역이 선택 되었습니다.")
            print()
            break
    else:
        print(f"{userInput} >> 해당 지역 없습니다.")
    return city
    

  
#subMenuChk-----------------------------------------------
def subMenuChk(city):
    
    if city in regionName:
        print(regionName.index(city))
        idx=regionName.index(city)
        print(idx)
        

        while True:
            print("-"*25, end="")
            print(f"{city}지역 데이터 개수[{regionDbSet(idx)}]", end="")
            print("-"*25)
            print()
            print("1. 데이터 확인  2. 최고기온 DATA  3.월 최고/최저기온 Data  4. 날짜 최고기온 Data  5.년도범위 날짜 최고기온 Data 6.일별 최고기온")
            print("-"*77)
            print()
            userInput=input("서브메뉴 번호를 입력하세요 [Q: 서브메뉴 종료]:")
            if userInput=="1":
                print()
                regionPagingData()
            elif userInput=="2":
                print()
                fildMaxChk(city)
            elif userInput=="3":
                monthMaxMinChk()
            elif userInput=="4":
                print()
                choiceFieldData()
            elif userInput=="5":
                print()
                yeardata()

            elif userInput=="6":
                dataBetWeenChk()
            elif userInput=="7":
                choiceTemper()
            elif userInput=="8":
                choiceMonth()
            elif userInput=="9":
                monthot()
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
    file=open(f"_dataSetGilBut01/{temperRegionFileList[idx]}","r",encoding="cp949")
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

def fildMaxChk(city):
    temperatureMaxDataSet=[]
    if city in regionName:
        #print(regionName.index(city))
        idx=regionName.index(city)
    for i in temperatureFileList:
        temperatureMaxDataSet.append(float(i[4]))
    print(temperatureMaxDataSet)
    print("서울^ Temperature Data MaxField Chk!")
    print(f"기상관측 이래 {city}의 최고기운 DataSet은{regionDbSet(idx)}개 입니다.")
    plt.figure(figsize=(9,2),dpi=200)
    plt.plot(temperatureMaxDataSet,'r')
    plt.show()
    
#-----------------------------------------------------------------------------------------------
def dataBetWeenChk():
    print()
    startDate=input("\t\t시작년도:")
    print()
    endDate=input("\t\t종료년도:")
    print()
    for i in temperatureFileList:
        if startDate==i[0][:4]:
            startD=temperatureFileList.index(i)
        if endDate==i[0][:4]:
            endD=temperatureFileList.index(i)
    temp=temperatureFileList[startD:endD]
    
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

def moreThanPlus30():
    vMonth=["01","02","03","04","05","06","07","08","09","10","11","12"]
    for monthIdx in vMonth:
        plus30=[]
        for i in temperatureFileList:
            if i[0][5:7]==monthIdx:
                if float(i[4]) >= 30.0:
                    plus30.append(i)
        print(f"기상관측 아래 {city}의 {monthIdx}월 영상 30도 이상 일수는 {len(plus30)}일입니다")
        print()


def lessThanMinus10():
    vMonth=["01","02","03","04","05","06","07","08","09","10","11","12"]
    for monthIdx in vMonth:
        less10=[]
        for i in temperatureFileList:
            if i[0][5:7]==monthIdx:
                if float(i[3]) <= -10.0:
                    less10.append(i)
        print(f"기상관측 아래 {city}의 {monthIdx}월 영하 10도 이하 일수는 {len(less10)}일입니다")
        print()

def choiceTemper():
    userInput=input("확인할 기온을 입력하세요. Ex] 30 / -10 [Q : 메뉴종료]:")
    vMonth=["01","02","03","04","05","06","07","08","09","10","11","12"]
    if userInput.upper()=="Q":
        return
    elif int(userInput) >= 0:
        for monthIdx in vMonth:
            userTemper=[]
            for i in temperatureFileList:
                if i[0][5:7]==monthIdx:
                    if float(i[4]) >= float(userInput):
                        userTemper.append(i)
            print(f"기상관측 아래 {city}의 {monthIdx}월 영상 {userInput}도 이상 일수는 {len(userTemper)}일입니다")
            print()
    elif int(userInput) < 0:
        for monthIdx in vMonth:
            userTemper=[]
            for i in temperatureFileList:
                if i[0][5:7]==monthIdx:
                    if float(i[3]) <= float(userInput):
                        userTemper.append(i)
            print(f"기상관측 아래 {city}의 {monthIdx}월 영하 {userInput}도 이하 일수는 {len(userTemper)}일입니다")
            print()
    

def choiceMonth():
    while True:
        
        userInput=input("확인할 월을 입력하세요. Ex] 01 or 12 [Q : 메뉴종료]:")
        if userInput.upper()=="Q":
            return
        else: 
            monthMaxData=[]
            monthMinData=[]
        
            dateMax=-9999
            dateMin=9999
            for i in temperatureFileList:
                if i[0][5:7]==userInput:
                    if dateMax < float(i[4]):
                        dateMax=float(i[4])
                        hotMonth=i
                    if dateMin > float(i[3]):
                        dateMin=float(i[3])
                        coldMonth=i
            monthMaxData.append(hotMonth)
            monthMinData.append(coldMonth)
          
            print(f"기상관측 아래 {city}의 {userInput}월 최고 기온은 {monthMaxData[0][0]}으로 {monthMaxData[0][4]}도 입니다")
            print(f"기상관측 아래 {city}의 {userInput}월 최저 기온은 {monthMinData[0][0]}으로 {monthMinData[0][3]}도 입니다")
            print()


def choiceFieldData():
    while True:
        userInput=input('확인할 날짜를 입력하세요. (01-01 ~ 12-31) : ')
        if userInput.upper() == 'Q':
            return        
        else : 
            choiceData = []
            for i in temperatureFileList:
                if userInput == i[0][5:10]:
                    choiceData.append(i)
                    maxT = float(-9999)
                    minT = float(9999)
                    for x in choiceData:
                        if float(maxT) < float(x[2]):
                            maxT = x[2]
                            dayHot=x[0],x[2]
                        if float(minT) > float(x[3]):
                            minT = x[3]
                            dayCold=x[0],x[3]

            print(f'기상관측 아래 {city}의 {userInput} 일 최고 기온 데이터는 {dayHot} 입니다.')
            print(f'기상관측 아래 {city}의 {userInput} 일 최저 기온 데이터는 {dayCold} 입니다.')
            
            
            
def yeardata():
    yearstart = input('시작년도 Ex] 2000 [Q: 메뉴종료] : ')
    yearend = input('종료년도 Ex] 2021 [Q: 메뉴종료] : ')
    yeardate = input('확인할 날짜를 입력하세요. Ex] 02-14 or 03-01 [Q : 메뉴종료] ')
    yearHot = []
    yearCold = []
    year = []
    
    for i in temperatureFileList:
        if yeardate == i[0][5:]:
            if yearstart <= i[0][0:4]:
                if yearend >= i[0][0:4]:
                    yearHot.append(i[4])
                    yearCold.append(i[3])
                    year.append(i[0][0:4])

    print(f'{yearstart}년 ~ {yearend}년  {yeardate} 데이터 개수는 {len(year)}개 입니다.')


    
    plt.figure(figsize = (9,2), dpi = 200)
    font_name=fm.FontProperties(fname="font\H2MJRE.TTF").get_name()
    plt.rc("font",family=font_name)#글꼴 설정
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(year, yearHot, 'hotpink', label = '최고기온')
    plt.plot(year, yearCold, 'skyblue', label = '최저기온')
    plt.legend(fontsize=7)
    plt.xticks(fontsize=7, color='#FF0000')
    plt.yticks(fontsize=7, color='#0000FF')
    plt.yticks([-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35])
    plt.ylim(-35,40)
    plt.grid(True)
    plt.show()
    
def monthot():
    vmonth = input('확인할 월을 입력하세요')
    for i in temperatureFileList:
        if i[0][5:7] == vmonth:
            for x in range(1,32):
                if i[0][9:11] == x:
                    print(i)
            
            
            

   

# # plt.figure(dpi = 300)
# plt.figure(figsize=(20,5))

# # 한글처리를 위해 폰트 설정
# font_name = font_manager.FontProperties(fname = "./../_Font/HYBSRB.TTF").get_name()

# plt.rc('font', family = font_name) # 맑은 고딕을 기본 글꼴로 설정

# plit.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지


while True:
    regionTitle()
  
    city=subMenuTitle()
  
    subMenuChk(city)