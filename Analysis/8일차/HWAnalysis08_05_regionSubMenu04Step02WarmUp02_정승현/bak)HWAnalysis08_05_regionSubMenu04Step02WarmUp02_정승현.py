import csv
from os import replace
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
populRegionFileList = ['populationSeoul.csv', 'populationBusan.csv',
		'populationDaegu.csv', 'populationIncheon.csv', 
		'populationGwangju.csv','populationDaejeon.csv', 
		'populationUlsan.csv', 'populationSejong.csv',

		'populationGyeonggi.csv', 'populationGangwon.csv', 'populationChungbuk.csv',
		'populationChungnam.csv', 'populationJeonbuk.csv', 'populationJeonnam.csv',
		'populationGyeongbuk.csv','populationGyeongnam.csv','populationJeju.csv'
		]
submenu = ["1.데이터 확인", " 2.현재지역확인", " 3.전체구간확인"," 4.MenuChk"," 5.MenuChk"," 6.MenuChk"]
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


f = open('./_dataSetGilBut01/population202202.csv','r',encoding='cp949')
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
                return
            elif userInput == '1':
                regionPagingData(idx)
            elif userInput =="2":
                regionChk(idx)
            elif userInput =="3":
                regionDbSet(idx)
            elif userInput == "4":
                regionSection02(idx)
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
	file=open('./_dataSetGilBut01/'+populRegionFileList[idx],'r',encoding='cp949')
	regionData = csv.reader(file)
	vRegionData=list(regionData)
	

	dataPerPage=int(input("한 페이지당 출력할 레코드 수를 입력하세요:"))
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
			dataOfBeginPage=(int(nowPage)-1)*dataPerPage
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
    stIdx = 2
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
            if int(userInput) == 1:
                stIdx = 2
            #     print(f"{sec02GuGunUK[int(userInput)]} {sec03EupMyeonDong[int(userInput)]} / {len(sec03EupMyeonDong[int(userInput)])+1}")

            if vuserInput < int(userInput):
                print()
                print()
                #print(f"{sec02GuGunUK[int(userInput)]} {sec03EupMyeonDong[int(userInput)]} / {len(sec03EupMyeonDong[int(userInput)])+1}")
                stIdx += len(sec03EupMyeonDong[int(vuserInput)])+1
                vuserInput += 1
            elif vuserInput == userInput:
                break
        for y in range(0,len(sec03EupMyeonDong[int(userInput)])):
            print(f"{y+1}.{sec03EupMyeonDong[int(userInput)][y]}")
        print()
        print(stIdx)
	
        file=open('./_dataSetGilBut01/'+populRegionFileList[idx],'r',encoding='cp949')
        regionData = csv.reader(file)
        populationRegionFileList=list(regionData)
        print(populationRegionFileList[stIdx])
    
        
            

            

        

        
   
   
        


    
#------------------------------------------------------------------------------------------------------------------------------------
while True:
				regionTitle()
				idx = menu()
				Submenu(idx)