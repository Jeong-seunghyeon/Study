import csv
import matplotlib
import pandas as pd
import numpy as np

populationfile = []

siDoGuGunList = []

siDoList = []
soDoNoList = []

siDoNoUK = []   # UK 는 Unique
siDoUK = []

tempSidoNo = -1

regionMenu = []

menu = []

tempRegion = []
totalRecSu = []

sec02GuGunUK = []
sec02GuGunNoUK = []

sec03EupMyeonDong = [] 
sec03EupMyeonDongNo = []
populationRegionFileList = []

populRegionFileList = ['populationGenderSeoul.csv', 'populationGenderBusan.csv',
        'populationGenderDaegu.csv', 'populationGenderIncheon.csv', 
        'populationGenderGwangju.csv','populationGenderDaejeon.csv', 
        'populationGenderUlsan.csv', 'populationGenderSejong.csv',

        'populationGenderGyeonggi.csv', 'populationGenderGangwon.csv', 'populationGenderChungbuk.csv',
        'populationGenderChungnam.csv', 'populationGenderJeonbuk.csv', 'populationGenderJeonnam.csv',
        'populationGenderGyeongbuk.csv','populationGenderGyeongnam.csv','populationGenderJeju.csv'
        ]

tempRegion = []



#-----------------------------------------------------------------------------------------

file=open(f"_dataSetGilBut01\population202202Gender.csv","r",encoding="cp949")
file=csv.reader(file)

for row in file:
    populationfile.append(row)

# print(len(populationfile))

vData = np.array(populationfile)
print(len(populationfile))
print(vData.shape)
print(populationfile[0][103])
#print(len(populationfile[0]))


for x in populationfile:
    if tempSidoNo != (x[0][-11:-9]):
        if x[0][0] == '행':
            pass
        else:
            siDoUK.append(x[0][0:-14])
            siDoNoUK.append(x[0][-11:-9])
            tempSidoNo = x[0][-11:-9]
    elif tempSidoNo == (x[0][-11:-9]):
        pass
    
# print(siDoUK)
# print(siDoNoUK)

for y in range(len(siDoUK)):
    regionMenu.append(siDoUK[y]+":"+siDoNoUK[y][0:2])
    
    
for i in range(len(regionMenu)):
    vmenu=regionMenu[i].split(",")
    menu.append(vmenu)

f = open('./_dataSetGilBut01/population202202Gender.csv','r',encoding='cp949')
data = csv.reader(f)
next(data)
populationFileList = list(data)
siDoNoList = []
#----------------------------------------------------------------------------------------

# for idx in range(len(populRegionFileList)):
#     dataSet = open(f'C:\_pythontest01\Analysis\_dataSetGilBut01\population202202.csv','r','cp949')
#     dataSet.close()

# for fileIdx in range(len(populRegionFileList)):
#     dataSet = open(f'_dataSetGilBut01/{populRegionFileList[fileIdx]}','w',newline='',encoding = "cp949")
#     dataSet.close()
    

# def regionFileSet() :
#     totalRecSu = []          
#     tempSiDoNo    = -1
#     populRegionFileIdx = 0
#     while True:
#         for x in range(len(populationfile)) :
#             tempRegion = []
#             vpop = populationfile[x][0].split()
#             if vpop[0] == siDoUK[populRegionFileIdx] :
#                 if vpop[0] =='행정구역':
#                     pass
#                 else:
#                     tempRegion.append(populationfile[x])
#                     dataSet = open(f'_dataSetGilBut01/{populRegionFileList[populRegionFileIdx]}','a',newline='',encoding = "cp949")
#                     wr = csv.writer(dataSet)
#                     wr.writerow(populationfile[x])
#         populRegionFileIdx += 1
#         if populRegionFileIdx == 17:
#             break
#         dataSet.close()
                

#     for idx in range(len(populRegionFileList)):
#         f = open(f'_dataSetGilBut01/{populRegionFileList[idx]}','r',encoding='cp949')
#         vf = csv.reader(f)
#         b = []
#         for a in vf:
#             b.append(a)
#             c = (b[0][0].split())
#         totalRecSu.append(c[0]+':'+str(len(b)))   


    
        

        
        
#     for idx in range(len(populRegionFileList)):
#         f = open(f'_dataSetGilBut01/{populRegionFileList[idx]}','r',encoding = "cp949" )
def regionFileSet():          
	tempSiDoNo = ""
	populRegionFileIdx = -1
	for idx in range(len(populRegionFileList)):
		dataSet = open('./_dataSetGilBut01/'+populRegionFileList[idx],'w',encoding='cp949')
		dataSet.close()
	for idx, populationLineList in enumerate(populationFileList):
		for colIdx in range(1,len(populationLineList)):
			populationLineList[colIdx] = populationLineList[colIdx].replace(",","")
		siDoGuGunList.append(populationLineList[0])
		tempSiDo = populationLineList[0].split()
		siDoList.append(tempSiDo[0])
		siDoNoList.append(tempSiDo[-1][-11:-1])
		if (siDoNoList[idx][:2] != tempSiDoNo):
			populRegionFileIdx +=1
			totalRecSu.append(0)
			tempSiDoNo = siDoNoList[idx][:2]
			siDoNoUK.append(siDoNoList[idx])
			siDoUK.append(siDoList[idx])
			#print(populRegionFileIdx)
	 
			dataSet = open('./_dataSetGilBut01/'+populRegionFileList[populRegionFileIdx],'a',encoding='cp949')
			tempwrite =",".join(populationLineList)+"\n"
			dataSet.write(tempwrite)
			totalRecSu[populRegionFileIdx] +=1
			dataSet.close()
		else:
			dataSet = open('./_dataSetGilBut01/'+populRegionFileList[populRegionFileIdx],'a',encoding='cp949')
			tempwrite =",".join(populationLineList)+"\n"
			dataSet.write(tempwrite)
			totalRecSu[populRegionFileIdx] +=1
			dataSet.close()
		
	#for idx in range(len(populRegionFileList)):
		#print(f'{siDoUK[idx]} : {totalRecSu[idx]}')  
        
                

regionFileSet()
#------regionTitle--------------------------------------------
def regionTitle():
    print("{0:=^91}\n".format("인구 공공데이터 분석 프로젝트 Ver01. "))
    cnt = 0
    for idx in range(17):
        siDoNoUK[idx] = siDoNoUK[idx][:2]
        siDoLen = len(siDoUK[idx]) + (14 - (len(siDoUK[idx])*2))
        print(f"[{siDoUK[idx]:<{siDoLen}}:{siDoNoUK[idx]}]",end="")
        cnt +=1
        
        if cnt%4 == 0:
            print()
    print("\n")

    # print(menu[0:4])
    # print(menu[4:8])
    # print(menu[8:12])
    # print(menu[12:16])
    # print(menu[16:])
    # print('='*98)

#--subMenuTitle---------------------------------------
def subMenuTitle():
    city=""
    userInput=input("\t\t메뉴의 번호를 입력하세요 [Q: 메뉴종료]:")
    if userInput.upper()=="Q":
        exit()
    for idx in range(len(siDoNoUK)):
        print(siDoNoUK[idx])
        if userInput==siDoNoUK[idx]:
            idxChk=idx
            city=siDoUK[idxChk]
            print()
            print(f"\t\t^{siDoUK[idxChk]} 지역이 선택 되었습니다.")
            print()
            break
    else:
        print(f"{userInput} >> 해당 지역 없습니다.")
    return city


#subMenuChk-----------------------------------------------


def subMenuChk(city):
    
    if city in siDoUK:
        #print(siDoUK.index(city))
        idx=siDoUK.index(city)
        
        
        while True:
            print("-"*25, end="")
            print(f"{city}지역 데이터 개수", end="")
            print("-"*25)
            print()
            print("1. 데이터 확인  2. 현재지역확인  3.전체구간 확인  4. 구간별 확인  5.MenuChk 6.MenuChk")
            print("-"*77)
            print()
            userInput=input("서브메뉴 번호를 입력하세요 [Q: 서브메뉴 종료]:")
            if userInput == '1':
                regionPagingData(idx)
            elif userInput == '2':
                regionChk(idx)
            elif userInput == '3':
                regionDbSet(idx)
            elif userInput == '4':
                regionSection03(idx)
            elif userInput == '5':
                print('MenuChk 확인')
            elif userInput == '6':
                print('MenuChk 확인')
            elif userInput.upper() == 'Q':
                print('서브메뉴를 종료합니다.')
                break
            else:
                print('해당없음')

#gettotal-------------------------------------------
def getTotalPage(m, n):
	if m % n == 0:
		return m // n
	else:
		return m // n + 1
#페이징----------------------------------------------------------------------------------------------------------------------------
def regionPagingData(idx):
	file=open('./_dataSetGilBut01/'+populRegionFileList[idx],'r',encoding='cp949')
	regionData = csv.reader(file)
	vRegionData=list(regionData)
	

	dataPerPage=(input("한 페이지당 출력할 레코드 수를 입력하세요:"))
	if type(dataPerPage) == int:
		dataPerPage = int(dataPerPage)
	elif dataPerPage.upper() == 'Q':
		return subMenuChk(city)
    
	totalPage=getTotalPage(totalRecSu[idx], dataPerPage)
	

	print("-"*50)
	print(f"기온 공공데이터 개수{totalRecSu[idx]}")
	print(f"기온 공공데이터 페이지 개수: {totalPage}")
	print("-"*50)

	Page=0
	tempPage=1
	while True:
		print(f"Enter를 치면 다음 {tempPage}/{totalPage} 페이지 {dataPerPage}개 레코드 확인") 
		nowPage=input("확인할 페이지를 입력 또는 Enter[Q:종료]:")
		if nowPage.upper()=="Q":
			print("종료합니다.")
			break
		else :#nowPage==""
			if tempPage==totalPage:
				print("마지막 페이지입니다.")
			elif tempPage < totalPage:
				for dataOfBeginPage in range(Page,(Page+dataPerPage)):
					print(f"{dataOfBeginPage+1}/{totalRecSu[idx]}  {dataOfBeginPage+1}번째 {vRegionData[dataOfBeginPage]}")
					Page+=1
				tempPage+=1
				print("-"*50)
		# else:
		# 	dataOfBeginPage=(int(nowPage)-1)*dataPerPage
		# 	for dataOfBeginPage in range((dataOfBeginPage),(dataOfBeginPage+dataPerPage)):
		# 		if dataOfBeginPage > len(totalRecSu)-1:
		# 			print()
		# 			print("확인할 수 있는 페이지 초과입니다")
		# 			break
		# 		else:
		# 			print(f"{dataOfBeginPage}/{totalRecSu}  {dataOfBeginPage}번째 {vRegionData[dataOfBeginPage]}")
		# 			tempPage=int(nowPage)


#현재지역확인---------------------------------------------------------------------------------------------------------------------
def regionChk(idx):
	print(f"	^{siDoUK[idx]} 지역이 선택 되었습니다.")
	print(f"{'-'*30} {siDoUK[idx]} 지역 데이터 개수 [{totalRecSu[idx]}] 확인 {'-'*30}")
	return
#전체구간확인---------------------------------------------------------------------------------------------------------------------
def regionDbSet(idx):
    global populationRegionFileList
    populationRegionFileList.clear()

    sec02GuGunUK.clear()
    sec02GuGunNoUK.clear()

    sec03EupMyeonDong.clear()
    sec03EupMyeonDongNo.clear()

    tempdo =""
    tempSec=[]
    secStartRow=[]
    tempguno = []
    tempeup =[]
    tempDongNo=[]
    sec02UkChk=-1

    file=open('./_dataSetGilBut01/'+populRegionFileList[idx],'r',encoding='cp949')
    regionData = csv.reader(file)
    populationRegionFileList=list(regionData)

    for i, regionlist in enumerate(populationRegionFileList):
        # print(i, regionlist[0])
        temp=regionlist[0].split()
        # print(temp)
        tempguno.append(temp[-1][-9:-7])
        sec03EupMyeonDongNo.append(temp[-1][-9:-1])
        if tempguno[i][:2] != tempdo:
            sec02UkChk+=1
            tempSec.append(1)
            sec02GuGunUK.append(temp[-2])
            tempdo=tempguno[i][:2]
            sec02GuGunNoUK.append(tempguno[i][:2])
            if sec02UkChk>0:
                sec03EupMyeonDong.append(tempeup)
                sec03EupMyeonDongNo.append(tempDongNo)
            tempeup=[]
            tempDongNo=[]
        else:
            tempSec[sec02UkChk]+=1
            tempeup.append(temp[-1][:-12])
            tempDongNo.append(temp[-1][-9:-1])
    sec03EupMyeonDong.append(tempeup)
    sec03EupMyeonDongNo.append(tempDongNo)
	# print(sec03EupMyeonDongNo)
	# print(sec03EupMyeonDong)
	# print(tempSec)
    for x in range(len(sec02GuGunUK)-1):
        if x==0:
            print()
            print(f"{sec02GuGunUK[0]}  {len(sec02GuGunNoUK)-1}개 구군 확인")
        else:
            print(f"[{sec02GuGunUK[x]} No : {sec02GuGunNoUK[x]}] >>> {len(sec03EupMyeonDong[x])}개 읍면동 ")
		# print()
        for y in range(len(sec03EupMyeonDong[x])):
            if y%5 == 0:
                print()
                print(sec03EupMyeonDong[x][y], end=" " )
            else:
                print(sec03EupMyeonDong[x][y], end=" " )
        print()
        print()
        print()
  
        print("Total_읍면동",":", sum(tempSec))

def regionSection02(idx):
    print(f'    >>> {siDoUK[idx]}No : {siDoNoUK[idx][0:2]} ] {len(sec02GuGunUK)-1}개 Section02 확인')
    for x in range(1,len(sec02GuGunUK)):
        print(f"{x}]{sec02GuGunUK[x]}")
    userInput = (input( '메뉴의 번호를 입력해 주세요. [ Q : 메뉴종료 ]: '))
    if userInput.upper() == 'Q':
        regionSection02(idx)
    elif int(userInput) > len(sec02GuGunUK):
        print('입력한 값을 확인하세요.')
    
    else:
        vuserInput = 1
        print(f"{int(userInput)}.{sec02GuGunUK[int(userInput)]} No.{sec02GuGunNoUK[int(userInput)]} {len(sec03EupMyeonDong[int(userInput)])}개 지역이 선택되었습니다.")
        for q in range(len(userInput)+len(sec03EupMyeonDong[int(vuserInput)])):
            if vuserInput <= int(userInput):
                print()
                print()
                print(f"{sec02GuGunUK[int(vuserInput)]} {sec03EupMyeonDong[int(vuserInput)]} / {len(sec03EupMyeonDong[int(vuserInput)])+1}")
                vuserInput += 1
            elif vuserInput == userInput:
                print(sec03EupMyeonDong.index(sec03EupMyeonDong[userInput][0]))
                break

def regionSection03(idx):
    
    #print(f'    >>> {siDoUK[idx]}No : {siDoNoUK[idx][0:2]} ] {len(sec02GuGunUK)-1}개 Section02 확인')
    
    for x in range(1,len(sec02GuGunUK)):
        if x < 10 :
            print(f"{x}]{sec02GuGunUK[x]}",end='  ')
        if x == 10:
            print(f"{x}]{sec02GuGunUK[x]}",end='  ')
            print()
        if x > 10:
            print(f"{x}]{sec02GuGunUK[x]}",end='  ')
        if x ==20:
            
            print()
        if x > 20:
            print(f"{x}]{sec02GuGunUK[x]}",end='  ')
        if x == 30:
            print()
        if x>30:
            print(f"{x}]{sec02GuGunUK[x]}",end='  ')
            
    print()
    while True:
        stIdx = 2
        print(f'    >>> {siDoUK[idx]}No : {siDoNoUK[idx][0:2]} ] {len(sec02GuGunUK)-1}개 Section02 확인')
        userInput	 = (input( '메뉴의 번호를 입력해 주세요. [ Q : 메뉴종료 ]: '))
    
        if userInput.upper() == 'Q':
            break
        elif int(userInput) > len(sec02GuGunUK):
            print('입력한 값을 확인하세요.')
    
        else:
            vuserInput = 1
        
            print(f"{int(userInput)}.{sec02GuGunUK[int(userInput)]} No.{sec02GuGunNoUK[int(userInput)]} {len(sec03EupMyeonDong[int(userInput)])}개 지역이 선택되었습니다.")
            for q in range(len(userInput)+len(sec03EupMyeonDong[int(vuserInput)])):
                if vuserInput < int(userInput):
                    print()
                    print()
                    #print(f"{0:<10}{sec02GuGunUK[int(vuserInput)]} {sec03EupMyeonDong[int(vuserInput)]} / {len(sec03EupMyeonDong[int(vuserInput)])+1}")
                    stIdx += len(sec03EupMyeonDong[int(vuserInput)])+1
                    vuserInput += 1
                elif vuserInput == userInput:
                    break
                if int(userInput) == 1:
                    stIdx = 2
            #print(f"{0:<10}{sec02GuGunUK[int(userInput)]} {sec03EupMyeonDong[int(userInput)]} / {len(sec03EupMyeonDong[int(vuserInput)])+1}")
            print()
            print('-'*30)
            for y in range(0,len(sec03EupMyeonDong[int(userInput)])):
                if y <8 :
                    print(f"{y+1}.{sec03EupMyeonDong[int(userInput)][y]}", end='  ')
                elif y == 8:
                    print(f"{y+1}.{sec03EupMyeonDong[int(userInput)][y]}", end='  ')
                    print()
                elif y > 8:
                    print(f"{y+1}.{sec03EupMyeonDong[int(userInput)][y]}", end='  ')
                elif y == 16:
                    print(f"{y+1}.{sec03EupMyeonDong[int(userInput)][y]}", end='  ')
                    print()
                elif y > 16:
                    print(f"{y+1}.{sec03EupMyeonDong[int(userInput)][y]}", end='  ')
            print()
            print()
            
            #print(f"인덱스값 : {stIdx}")
            vpopulationRegionFileList=[]
            file=open('./_dataSetGilBut01/'+populRegionFileList[idx],'r',encoding='cp949')
            regionData = csv.reader(file)
            populationRegionFileList=list(regionData)
            #print(populationRegionFileList)
            
            
                
            #print(populationRegionFileList[stIdx])
            userInput2 = input('읍면동 메뉴의 번호를 입력하세요. [Q : 메뉴종료 ] : ')
            ageIdx = 10
            ageIdx1 = 0
            sumIdx = 0
            vsumIdx = []
            vvsumIdx = []
            realIdx = 9
            MaxIdx = []
            Man = []
            Woman = []
            vwomansumidx = []
            vvwomansumidx = []
            WMaxIdx = []
            MsortIdx = []
            WosortIdx = []
            
            ageRangeList = ["00-09세","10-19세","20-29세","30-39세","40-49세","50-59세","60-69세","70-79세","80-89세","90-99세","100세 이상"]
            ageRangeListCnt = []
            for ageIdx0 in range(len(ageRangeList)):
                ageRangeListCnt.append(0)
            realAge = []
            print(populationRegionFileList[stIdx+int(userInput2)-1])
            Man.append(populationRegionFileList[stIdx+int(userInput2)-1][3:104])
            Woman.append(populationRegionFileList[stIdx+int(userInput2)-1][106:])
            #print(Man)
            #print(Woman)
            #--[인구분석----------------------------------------------------------------------------]
            print(f"컬럼개수 : {len(populationRegionFileList[stIdx+int(userInput2)-1])}")
            print(f"행정구역 : {populationRegionFileList[stIdx+int(userInput2)-1][0]}")
            print(f"총인구수 : {int(populationRegionFileList[stIdx+int(userInput2)-1][1]) + int(populationRegionFileList[stIdx+int(userInput2)-1][104])}")
            print(f"연령구간인구수 : {int(populationRegionFileList[stIdx+int(userInput2)-1][1]) + int(populationRegionFileList[stIdx+int(userInput2)-1][104])}")
            print(f"남성 총 인구수 : {populationRegionFileList[stIdx+int(userInput2)-1][1]}")
            print(f"여성 총 인구수 : {populationRegionFileList[stIdx+int(userInput2)-1][104]}")
            for x in range(3,len(populationRegionFileList[stIdx+int(userInput2)-1])):
                realAge.append(f"{populationRegionFileList[stIdx+int(userInput2)-1][x]}")
            #print(populationRegionFileList[stIdx+int(userInput2)-1])
            #print(realAge)
            for y in range(len(ageRangeListCnt)):
                mansumIdx = 0
                womansumIdx = 0
                if ageIdx <= 100 :
                    print(f"남성 {ageRangeList[y]} : {realAge[ageIdx1:ageIdx]}")
                    print(f"여성 {ageRangeList[y]} : {realAge[ageIdx1+103:ageIdx+103]}")
                    #print(f"합 : {realAge[ageIdx1:ageIdx]}")
                    for z in range(len(ageRangeListCnt)-1):
                        mansumIdx += int(realAge[ageIdx1:ageIdx][z])
                        vsumIdx.append(mansumIdx)
                        womansumIdx += int(realAge[ageIdx1+103:ageIdx+103][z])
                        vwomansumidx.append(womansumIdx)
                    vvsumIdx.append(vsumIdx[realIdx])  
                    vvwomansumidx.append(vwomansumidx[realIdx])  
                    print(f"남성 합 : {vvsumIdx[y]}")
                    print(f"여성 합 : {vvwomansumidx[y]}")
                    print(f"전체 합 : {vvsumIdx[y] + vvwomansumidx[y]}\n\n")
                    
                    #print(sortIdx)
                    #print(sortIdx.index(vvsumIdx[y]))
                    ageIdx += 10
                    ageIdx1 += 10
                    realIdx += 10
                    
                else:
                    print(f"\n 남성 {ageRangeList[-1]} : {realAge[100]}")
                    print(f"여성 {ageRangeList[-1]} : {realAge[203]}")
                    vvsumIdx.append(int(realAge[100]))
                    vvwomansumidx.append(int(realAge[203]))
                    print(f"남성 합 : {realAge[100]}")
                    print(f"여성 합 : {realAge[203]}")
                    print(f"전체 합 : {int(realAge[100]) + int(realAge[203])}")
            sortIdx=sorted(vvsumIdx, reverse=True)
            wsortIdx=sorted(vvwomansumidx, reverse=True)
            print()
            print()
            for z in range(len(vvsumIdx)):
                #print(f"남성등위 {sortIdx.index(vvsumIdx[z])}",end='  ')
                MsortIdx.append(sortIdx.index(vvsumIdx[z]))
                #print(f"여성등위{ageRangeList[z]} : {wsortIdx.index(vvwomansumidx[z])} 위",end='  ')
                if sortIdx.index(vvsumIdx[z]) == 0:
                    MaxIdx.append(f"남성 최고인원 Chk : {ageRangeList[z]} : {sortIdx[0]} ")
                    #WMaxIdx.append(f"여성 최고인원 Chk : {ageRangeList[z]} : {wsortIdx[0]}")
            print()
            for Widx in range(len(vvwomansumidx)):
                #print(f"여성등위 {wsortIdx.index(vvwomansumidx[Widx])}",end='  ')
                WosortIdx.append(wsortIdx.index(vvwomansumidx[Widx]))
                if wsortIdx.index(vvwomansumidx[Widx]) == 0:
                    WMaxIdx.append(f"여성 최고인원 Chk : {ageRangeList[Widx]} : {wsortIdx[0]}")
            print()
            
            print('연령구간',end='')
            for XX in range(len(vvsumIdx)):
                # 남성 : {vvsumIdx[XX]} 여성 : {vvwomansumidx[XX]} \n
                print(f"  {ageRangeList[XX]}",end= '')
            print()
            print('남성',end='     ')
            for XXX in range(len(vvsumIdx)):
                print(f"{vvsumIdx[XXX]:>9}",end='')
            print()
            print('여성',end='     ')
            for XXXX in range(len(vvsumIdx)):
                print(f"{vvwomansumidx[XXXX]:>9}",end='')
            print()
            print('전체',end='     ')
            for XXXXX in range(len(vvsumIdx)):
                print(f"{int(vvsumIdx[XXXXX]) + int(vvwomansumidx[XXXXX]):>9}",end='')
            print()
            print(MaxIdx)
            print(WMaxIdx)
            print(f"남성 등위 {MsortIdx}")
            print(f"여성 등위 {WosortIdx}")
            print()
while True:
    regionTitle()
    city = subMenuTitle()
    subMenuChk(city)
    