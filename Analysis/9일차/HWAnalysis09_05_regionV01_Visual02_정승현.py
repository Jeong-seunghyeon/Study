import csv
from os import replace
import zipapp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
populRegionFileList = ['populationSeoul.csv', 'populationBusan.csv',
		'populationDaegu.csv', 'populationIncheon.csv', 
		'populationGwangju.csv','populationDaejeon.csv', 
		'populationUlsan.csv', 'populationSejong.csv',

		'populationGyeonggi.csv', 'populationGangwon.csv', 'populationChungbuk.csv',
		'populationChungnam.csv', 'populationJeonbuk.csv', 'populationJeonnam.csv',
		'populationGyeongbuk.csv','populationGyeongnam.csv','populationJeju.csv'
		]
submenu = ["1.데이터 확인",  " 2.현재지역확인",  " 3.전체구간확인" , " 4.구간별 확인\n\n"," 5.지역명 확인_BarChart",f"{'6.지역명 찾기_BarhCHart':>26}"]
siDoGuGunList = []
siDoList = [] #도시 이름(서울, 부산 광역시 등등)
siDoNoList = [] #도시 넘버(11,22 등)
siDoNoUK = [] 
siDoUK = []
tempSiDoNo = -1
tempRegion = []
totalRecSu = []

sec02GuGunUK = []
sec02GuGunNoUK = []

sec03EupMyeonDong = [] 
sec03EupMyeonDongNo = []
populationRegionFileList = []


f = open('_dataSetGilBut01\population202202.csv','r',encoding='cp949')
data = csv.reader(f)
next(data)
populationFileList = list(data)

#---------------------------dbset() 데이터 불러오기
def regionFileSet():
	tempSiDoNo = ""
	populRegionFileIdx = -1
	
	for idx, populationLineList in enumerate(populationFileList):
		#숫자형 표현
		for colIdx in range(1,len(populationLineList)):
			populationLineList[colIdx] = populationLineList[colIdx].replace(",","")
		# print(populationLineList)
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
			totalRecSu[populRegionFileIdx] +=1
		else:
			totalRecSu[populRegionFileIdx] +=1
regionFileSet()# 파일이 존재하고 그 안에 값이 존재 할 때 시작
#---------------------regionFileSet(): 데이터 불러와서 지역별로 나누기
def regionFileSet():          
	tempSiDoNo = ""
	populRegionFileIdx = -1
	for idx in range(len(populRegionFileList)):
		dataSet = open('Analysis\_dataSetGilBut01/'+populRegionFileList[idx],'w',encoding='cp949')
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
	 
			dataSet = open('Analysis\_dataSetGilBut01/'+populRegionFileList[populRegionFileIdx],'a',encoding='cp949')
			tempwrite =",".join(populationLineList)+"\n"
			dataSet.write(tempwrite)
			totalRecSu[populRegionFileIdx] +=1
			dataSet.close()
		else:
			dataSet = open('Analysis\_dataSetGilBut01/'+populRegionFileList[populRegionFileIdx],'a',encoding='cp949')
			tempwrite =",".join(populationLineList)+"\n"
			dataSet.write(tempwrite)
			totalRecSu[populRegionFileIdx] +=1
			dataSet.close()
		
	for idx in range(len(populRegionFileList)):
		print(f'{siDoUK[idx]} : {totalRecSu[idx]}')       
#regionFileSet() #지역별 파일이 없을때 돌리기
#-----------------------------------------------------------title
def regionTitle():
	chk = 0
	dochk = 0
	print('='*30,'기온 공공데이터 분석 프로젝트 Ver01.','='*30)    
	for x in range(len(siDoUK)):
		do = siDoUK[x].split()
		if do[0][-1] == "도" and dochk == 0:
			print()
			print()
			dochk +=1
		if chk == 4:
			print()
			print(f'[{siDoUK[x]}    : {siDoNoUK[x][:2]}] ', end="")
			chk = 0
		else:
			print(f'[{siDoUK[x]}    : {siDoNoUK[x][:2]}] ', end="")
		chk +=1
	print()
	print('='*99)
	
def menu():
	idx = -1 
	print()
	userInput=input("\t\t메뉴의 번호를 입력하세요 [Q: 메뉴종료]:")
	if userInput.upper()=="Q":
		exit()
	else:
		if userInput+'00000000' in siDoNoUK:
			for x in range(len(siDoNoUK)):
				if siDoNoUK[x][:2] == userInput:
					idx = x
					print(f"	^{siDoUK[x]} 지역이 선택 되었습니다.")
				 
		else:            
			print(f"	^{userInput} 없는 지역입니다.")
		
	return idx
def Submenu(idx):
    while True:
        if idx != -1:
            print('-'*30,siDoUK[idx],"지역 데이터 개수 [",totalRecSu[idx],"] 확인",'-'*30)
            print()
            for x in range(len(submenu)):
                print(submenu[x], end="")
            print()
            print('-'*98)
            userInput = input("\t\t서브메뉴의 번호를 입력하세요 [Q: 메뉴종료]:")
            if userInput.upper()=="Q":
                return regionTitle()
            elif userInput == '1':
                regionPagingData(idx)
            elif userInput =="2":
                regionChk(idx)
            elif userInput =="3":
                regionDbSet(idx)
            elif userInput == "4":
                regionSection02(idx)
            elif userInput == "5":
                regionName(idx)
            elif userInput =='6':
                regionName2(idx)
            else:
                print("\t 해당 번호 없음 확인!!")
        else:
            return
		
#gettotal-------------------------------------------
def getTotalPage(m, n):
	if m % n == 0:
		return m // n
	else:
		return m // n + 1
	
#페이징----------------------------------------------------------------------------------------------------------------------------
def regionPagingData(idx):
	file=open('Analysis\_dataSetGilBut01/'+populRegionFileList[idx],'r',encoding='cp949')
	regionData = csv.reader(file)
	vRegionData=list(regionData)
	

	dataPerPage=(input("한 페이지당 출력할 레코드 수를 입력하세요:"))
	if dataPerPage.upper() == 'Q':
		return Submenu(idx)
	else:
		totalPage=getTotalPage(totalRecSu[idx], int(dataPerPage))


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
		elif nowPage=="":
			tempPage+=1
			if tempPage==totalPage:
				print("마지막 페이지입니다.")
			else:
				for dataOfBeginPage in range(Page,(Page+dataPerPage)):
					print(f"{dataOfBeginPage}/{totalRecSu[idx]}  {dataOfBeginPage}번째 {vRegionData[dataOfBeginPage]}")
					Page+=1
				print("-"*50)
		else:
			dataOfBeginPage=int((int(nowPage))-1)*dataPerPage
			for dataOfBeginPage in range((dataOfBeginPage),(dataOfBeginPage+dataPerPage)):
				if dataOfBeginPage > totalRecSu-1:
					print()
					print("확인할 수 있는 페이지 초과입니다")
					break
				else:
					print(f"{dataOfBeginPage}/{totalRecSu}  {dataOfBeginPage}번째 {vRegionData[dataOfBeginPage]}")
					tempPage=int(nowPage)


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

    file=open('Analysis\_dataSetGilBut01/'+populRegionFileList[idx],'r',encoding='cp949')
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
    
    #print(f'    >>> {siDoUK[idx]}No : {siDoNoUK[idx][0:2]} ] {len(sec02GuGunUK)-1}개 Section02 확인')
    
    for x in range(1,len(sec02GuGunUK)):
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
                print(f"{y+1}.{sec03EupMyeonDong[int(userInput)][y]}", end='  ')
            print()
            print()
            
            #print(f"인덱스값 : {stIdx}")
	
            file=open('Analysis\_dataSetGilBut01/'+populRegionFileList[idx],'r',encoding='cp949')
            regionData = csv.reader(file)
            populationRegionFileList=list(regionData)
            #print(populationRegionFileList[stIdx])
            userInput2 = input('읍면동 메뉴의 번호를 입력하세요. [Q : 메뉴종료 ] : ')
            ageIdx = 10
            ageIdx1 = 0
            sumIdx = 0
            vsumIdx = []
            vvsumIdx = []
            realIdx = 9
            MaxIdx = []
            
            
            ageRangeList = ["00-09세","10-19세","20-29세","30-39세","40-49세","50-59세","60-69세","70-79세","80-89세","90-99세","100세 이상"]
            ageRangeListCnt = []
            for ageIdx0 in range(len(ageRangeList)):
                ageRangeListCnt.append(0)
            realAge = []
            print(populationRegionFileList[stIdx+int(userInput2)-1])
            print(f"컬럼개수 : {len(populationRegionFileList[stIdx+int(userInput2)-1])}")
            print(f"행정구역 : {populationRegionFileList[stIdx+int(userInput2)-1][0]}")
            print(f"총인구수 : {populationRegionFileList[stIdx+int(userInput2)-1][1]}")
            print(f"연령구간인구수 : {populationRegionFileList[stIdx+int(userInput2)-1][2]}")
            for x in range(3,len(populationRegionFileList[stIdx+int(userInput2)-1])):
                realAge.append(f"{populationRegionFileList[stIdx+int(userInput2)-1][x]}")
            
            for y in range(len(ageRangeListCnt)):
                sumIdx = 0
                if ageIdx <= 100 :
                    print(f"{ageRangeList[y]} : {realAge[ageIdx1:ageIdx]}")
                    #print(f"합 : {realAge[ageIdx1:ageIdx]}")
                    for z in range(len(ageRangeListCnt)-1):
                        sumIdx += int(realAge[ageIdx1:ageIdx][z])
                        vsumIdx.append(sumIdx)
                    vvsumIdx.append(vsumIdx[realIdx])    
                    print(f"합 : {vvsumIdx[y]}")
                    
                    #print(sortIdx)
                    #print(sortIdx.index(vvsumIdx[y]))
                    ageIdx += 10
                    ageIdx1 += 10
                    realIdx += 10
                    
                else:
                    print(f"{ageRangeList[-1]} : {realAge[-1]}")
                    vvsumIdx.append(int(realAge[-1]))
                    print(f"합 : {realAge[-1]}")
            sortIdx=sorted(vvsumIdx, reverse=True)
            print()
            print()
            for z in range(len(vvsumIdx)):
                print(f"{ageRangeList[z]} : {sortIdx.index(vvsumIdx[z])} 위",end='  ')
                if sortIdx.index(vvsumIdx[z]) == 0:
                    MaxIdx.append(f"최고인원 Chk : {ageRangeList[z]} : {sortIdx[0]} ")
            print()
            print(MaxIdx)
            
            print()

def regionName(idx):
    dong = []
    userInput = input(f"인구 구조가 알고싶은 지역의 이름(읍면동 단위)를 입력하세요 [ Q : 메뉴 종료 ] : ")
    file=open('_dataSetGilBut01/'+populRegionFileList[idx],'r',encoding='cp949')
    regionData = csv.reader(file)
    populationRegionFileList=list(regionData)
    for x in range(len(populationRegionFileList)):
        if userInput in populationRegionFileList[x][0]:
            print(populationRegionFileList[x])
            dong = (populationRegionFileList[x][3:])
        elif userInput.upper() == 'Q':
            Submenu(idx)

            

    vIdx = 0
    vdong=[]
    for y in dong:
        vdong.append(y.replace(',',''))
    
  
        
        
        
    for PopIdx in range(len(vdong)):
        if int(vIdx) <= int(vdong[PopIdx]):
            vIdx = vdong[PopIdx]
    print(vIdx)
    vAge = int(vdong.index(vIdx))
    print(f"최고인원 : {vAge}세 : {vIdx}명")
    
    
    
    
    xidx = []
    for z in range(len(vdong)):
        
        xidx.append(f"{z}세")
    dongIdx = list(map(int,vdong))
    font_name = fm.FontProperties(fname='font\HMKMRHD.TTF').get_name()
    plt.rc('font',family = font_name)
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize = (9,2), dpi = 200)
    plt.bar(range(101),dongIdx,label='연령 분포')
    plt.legend(fontsize=7)
    plt.xticks([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120])
    yIdx = []
    zIdx = 0
    for z in range(1,10):
        if int(vIdx) > zIdx :
            yIdx.append(zIdx)
            zIdx += 100
        elif int(vIdx) <= zIdx:
            zIdx = int(vIdx)
            yIdx.append(zIdx)
        elif int(vIdx) < 100:
            yIdx.append(zIdx)
            zIdx += 10
    plt.yticks(yIdx)
        
    plt.xticks(fontsize=5)
    plt.yticks(fontsize=5)
    plt.ylim(0,int(vIdx)+20)
    plt.grid(True)
    
    
    plt.show()
    
    
def regionSearch(idx):
    Dongs = []
    userInput = input('찾고자 하는 지역의 이름(읍면동 단위)을 입력하세요 [ Q : 메뉴종료 ] : ')
    for x in range(len(populRegionFileList)):
        f = open('_dataSetGilBut01/'+populRegionFileList[x],'r',encoding='cp949')
        regionData = csv.reader(f)
        vData = list(regionData)
        for y in range(len(vData)):
            if userInput in vData[y][0]:
                Dongs.append(vData[y][0])
                break
    for z in Dongs:
        print(Dongs.index(z)+1,z)
            
        
    # for x in range(len(populationFileList)):
    #     if userInput in populationFileList[x][0]:
    #         Dongs.append(populationFileList[x][0])
    # for y in Dongs:
    #     print(Dongs.index(y)+1,y)
    
    
def regionName2(idx):
    dong = []
    userInput = input(f"인구 구조가 알고싶은 지역의 이름(읍면동 단위)를 입력하세요 [ Q : 메뉴 종료 ] : ")
    file=open('_dataSetGilBut01/'+populRegionFileList[idx],'r',encoding='cp949')
    regionData = csv.reader(file)
    populationRegionFileList=list(regionData)
    for x in range(len(populationRegionFileList)):
        if userInput in populationRegionFileList[x][0]:
            print(populationRegionFileList[x])
            dong = (populationRegionFileList[x][3:])
        elif userInput.upper() == 'Q':
            Submenu(idx)

            

    vIdx = 0
    vdong=[]
    for y in dong:
        vdong.append(y.replace(',',''))
    
  
        
        
        
    for PopIdx in range(len(vdong)):
        if int(vIdx) <= int(vdong[PopIdx]):
            vIdx = vdong[PopIdx]
    print(vIdx)
    vAge = int(vdong.index(vIdx))
    print(f"최고인원 : {vAge}세 : {vIdx}명")
    
    
    
    
    xidx = []
    for z in range(len(vdong)):
        
        xidx.append(f"{z}세")
    dongIdx = list(map(int,vdong))
    font_name = fm.FontProperties(fname='font\HMKMRHD.TTF').get_name()
    plt.rc('font',family = font_name)
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize = (9,2), dpi = 200)
    plt.barh(range(101),dongIdx,label='연령 분포')
    plt.legend(fontsize=7)
    plt.yticks([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120])
    yIdx = []
    zIdx = 0
    for z in range(1,10):
        if int(vIdx) > zIdx :
            yIdx.append(zIdx)
            zIdx += 100
        elif int(vIdx) <= zIdx:
            zIdx = int(vIdx)
            yIdx.append(zIdx)
        elif int(vIdx) < 100:
            yIdx.append(zIdx)
            zIdx += 10
    plt.xticks(yIdx)
        
    plt.xticks(fontsize=5)
    plt.yticks(fontsize=5)
    plt.ylim(0,105)
    plt.grid(True, alpha=0.5)
    plt.show()
    
             
            
	
                
                
					
				
		
			
				

				

        

        
   
   
        


    
#------------------------------------------------------------------------------------------------------------------------------------
while True:
				regionTitle()
				idx = menu()
				Submenu(idx)