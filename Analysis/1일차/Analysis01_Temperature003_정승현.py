f = open('./_dataSetGilBut01/daejeon.csv','r', encoding='949')data = reader(f,delimiter=',')data1 = list(data)high = 0low = 0Avg = 0for tmpList in data1:	if tmpList[2]=='':		Avg+=1	if tmpList[3] =='':		low +=1	if tmpList[4] =='':		high +=1print('초기 데이터 개수 :',len(data1),'개')print('최고기온 데이터 개수 :',high,'개')print('최저기온 데이터 개수 :',low,'개')print('평균기온 데이터 개수 :',Avg,'개')