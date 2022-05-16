from codecs import xmlcharrefreplace_errors
import csv
from tkinter import Y
import matplotlib
from matplotlib.pyplot import xlim
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

populRegionFileList = ['populationSeoul.csv', 'populationBusan.csv',
        'populationDaegu.csv', 'populationIncheon.csv', 
        'populationGwangju.csv','populationDaejeon.csv', 
        'populationUlsan.csv', 'populationSejong.csv',

        'populationGyeonggi.csv', 'populationGangwon.csv', 'populationChungbuk.csv',
        'populationChungnam.csv', 'populationJeonbuk.csv', 'populationJeonnam.csv',
        'populationGyeongbuk.csv','populationGyeongnam.csv','populationJeju.csv'
        ]

tempRegion = []



#-----------------------------------------------------------------------------------------

file=open(f"./_dataSetGilBut01/population202202.csv","r",encoding="cp949")
file=csv.reader(file)

for row in file:
    populationfile.append(row)

# print(len(populationfile))

vData = np.array(populationfile)
# print(len(populationfile))
# print(vData.shape)


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
    
    
sec02GuGunUK = []
sec02GuGunNoUK = []

sec03EupMyeonDong = [] 
sec03EupMyeonDongNo = [] 

tempGuGunNo = -1
tempEupMyeonDongNo = -1
for y in populationfile:
    #print(y[0][-9:-7])
    #print(y[0][-6:-4])
    if tempGuGunNo != (y[0][-9:-7]):
        if y[0][0] =='행':
            pass
        else:
            a = (y[0].split())
            if len(a[1]) > 6 :
                pass
            else:
                sec02GuGunUK.append(a[1])
                sec02GuGunNoUK.append(a[-1][3:5])
                tempGuGunNo = y[0][-9:-7]
    elif tempGuGunNo == (y[0][-9:-7]):
        pass
            
for z in populationfile:
    if tempEupMyeonDongNo != z[0][-6:-4]:
        if z[0][0] =='행':
            pass
        else:
            b = z[0].split()
            if len(b[-1]) < 13:
                pass
            
            else:
                c = (b[-1].split('('))

                sec03EupMyeonDong.append(c[0])
                sec03EupMyeonDongNo.append(c[1][:10])
                tempEupMyeonDongNo = z[0][-6:-4]
    elif tempEupMyeonDongNo == z[0][-6:-4]:
        pass
    

                
    
            
            
#print(sec02GuGunNoUK)
#print(sec02GuGunUK)


    #     for z in a:
    #         #print(z)
    #     tempGuGunNo == y[0][-9:-7]
    # elif tempGuGunNo == y[0][-9:-7]:
    #     pass
    
#print(sec02GuGunUK)
        
# print(siDoUK)
# print(siDoNoUK)

for y in range(len(siDoUK)):
    regionMenu.append(siDoUK[y]+":"+siDoNoUK[y][0:2])
    
    
for i in range(len(regionMenu)):
    vmenu=regionMenu[i].split(",")
    menu.append(vmenu)


#----------------------------------------------------------------------------------------

# for idx in range(len(populRegionFileList)):
#     dataSet = open(f'C:\_pythontest01\Analysis\_dataSetGilBut01\population202202.csv','r','cp949')
#     dataSet.close()

# for fileIdx in range(len(populRegionFileList)):
#     dataSet = open(f'_dataSetGilBut01/{populRegionFileList[fileIdx]}','w',newline='',encoding = "cp949")
#     dataSet.close()
    

def regionFileSet() :
    totalRecSu = [] 
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
    # for colIdx in range(1,len(populationfile)):
    #     populationfile[colIdx] = populationfile[colIdx].replace(',','')
        
        
                

    for idx in range(len(populRegionFileList)):
        f = open(f'_dataSetGilBut01/{populRegionFileList[idx]}','r',encoding='cp949')
        vf = csv.reader(f)
        b = []
        for a in vf:
            b.append(a)
        Alldata = b
        tempRegion.append(len(b))
        c = (b[0][0].split())
        totalRecSu.append(c[0]+':'+str(len(b)))
    return (tempRegion[idx])

    
        


        

        
        
    # for idx in range(len(populRegionFileList)):
    #     f = open(f'_dataSetGilBut01/{populRegionFileList[idx]}','r',encoding = "cp949" )
        
                


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
        print(siDoUK.index(city))
        cityIdx=siDoUK.index(city)
        
        
        
        while True:
            print("-"*25, end="")
            print(f"{city}지역 데이터 개수 [{tempRegion[cityIdx]}]", end="")
            print("-"*25)
            print()
            print("1. 데이터 확인  2. 현재지역확인  3.전체 구간 확인  4. MenuChk  5.MenuChk 6.MenuChk")
            print("-"*77)
            print()
            userInput=input("서브메뉴 번호를 입력하세요 [Q: 서브메뉴 종료]:")
            if userInput == '1':
                print('데이터 확인')
                regionSubMenu(cityIdx)
            elif userInput == '2':
                print('현재지역확인')
            elif userInput == '3':
                print('전체 구간 확인')
                regionDbSet(cityIdx)
            elif userInput == '4':
                print('MenuChk 확인')
            elif userInput == '5':
                print('MenuChk 확인')
            elif userInput == '6':
                print('MenuChk 확인')
            elif userInput.upper() == 'Q':
                print('서브메뉴를 종료합니다.')
                break
            else:
                print('해당없음')
                
#-----------------------------------------------------------------------
def getTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1
 
 
#--------------------------------------------------------------------------   
def regionSubMenu(cityIdx):
    
    dataPerPage=int(input("한 페이지당 출력할 레코드 수를 입력하세요:"))
    totalPage=getTotalPage(tempRegion[cityIdx], dataPerPage)

    print("-"*50)
    print(f"기온 공공데이터 개수{tempRegion[cityIdx]}")
    print(f"기온 공공데이터 페이지 개수: {totalPage}")
    print("-"*50)
#----------------------------------------------------------------------------------------------
    Page=0
    tempPage=1
    file = open(f'_dataSetGilBut01/{populRegionFileList[cityIdx]}','r',encoding='cp949')
    vfile = csv.reader(file)
    vvfile = []
    for x in vfile:
        vvfile.append(x)
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
                    print(f"{int(dataOfBeginPage)+1}/{tempRegion[cityIdx]}  {int(dataOfBeginPage)+1}번째 {vvfile[dataOfBeginPage]}")
                    Page+=1
                print("-"*50)
        else:
            dataOfBeginPage=(int(nowPage)-1)*dataPerPage
            for dataOfBeginPage in range((dataOfBeginPage),(dataOfBeginPage+dataPerPage)):
                if dataOfBeginPage > tempRegion[cityIdx]-1:
                    print()
                    print("확인할 수 있는 페이지 초과입니다")
                    break
                else:
                    print(f"{dataOfBeginPage+1}/{tempRegion[cityIdx]}  {dataOfBeginPage+1}번째 {vvfile[dataOfBeginPage]}")
                    tempPage=int(nowPage)
        
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------

                
def regionDbSet(cityIdx):
    sec02GuGunUK.clear()
    sec02GuGunNoUK.clear()
    sec03EupMyeonDong.clear()
    sec03EupMyeonDongNo.clear()
    file = open(f'_dataSetGilBut01/{populRegionFileList[cityIdx]}','r',encoding='cp949')
    vfile = csv.reader(file)
    vvfile = []
    a = []
    gugunIdx = -1
    Eupmyeon = []
    sec02UkChk = -1
    Euptemp = 0
    Lentemp = ''
    vsec03EupMyeonDong = []
    
    
    
    for x in vfile:
        a.append(x[0].split())
    for y in a:
        if len(y[1]) >10:
            pass
        else:
            Eupmyeon.append(y[2].split('('))
            if gugunIdx != (y[2][-9:-7]):
                sec02GuGunUK.append(y[1])
                sec02GuGunNoUK.append(y[2][-9:-7])
                gugunIdx = (y[2][-9:-7])
                
                
            elif gugunIdx == (y[2][-9:-7]):
                
                
                
                for z in range(len(sec02GuGunUK)):
                    if sec02UkChk == y[2][-9:-7] :
                        if Lentemp != y[2]:
                            Lentemp = y[2]
                            sec03EupMyeonDong.append(y)
                            
                    elif sec02UkChk != y[2][-9:-7] :
                        
                        sec02UkChk = y[2][-9:-7]
                        pass
                pass

 
    print(sec03EupMyeonDong)
    
    
    # print(f"{len(sec02GuGunUK)+1} : {len(sec02GuGunNoUK)+1} : {len(sec03EupMyeonDong)+len(sec02GuGunNoUK)+1}")
    # for y in range(len(sec02GuGunUK)):
        # print(sec02GuGunUK[y]+sec02GuGunNoUK[y])

    # for x in range(len(sec02GuGunUK)):
    #     #print(sec03EupMyeonDong[x][1])
    #     try: 
    #         print(sec02GuGunUK[x],'[No : ',sec02GuGunNoUK[x],']', '>>> ', sec03EupMyeonDong[x][2],'\n\n') 
    #     except:
    #         pass
            

while True:
    
    regionTitle()
    city = subMenuTitle()
    totalRecSu = regionFileSet()
    subMenuChk(city)
