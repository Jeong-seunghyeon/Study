#HWPython14_09_Recommend_정승현.py

Name = ['민교','강경태', '고재호', '김태인', '한현기','재호','민교','재호','선웅','박연희','민교', '선웅', '강경태', '고재호', '김태인', '한현기', '이준혁','민교', '선웅','임재우','민교','강경태','경태','경태']
NameChk = []
vNum=[]

for x in Name:
	if len(x) == 2:
		NameChk.append(x)
	
	else:
		NameChk.append(x[1:])

#print(NameChk)
NameChk.sort(reverse=False) # 정렬


vName = list(set(NameChk)) #중복제거

#print(vName) 



for x in vName:
	#print(x,NameChk.count(x),'표')
	vNum.append(NameChk.count(x))
vNum.sort(reverse=False)

for x in  range(len(vNum)-1) :
	for y in range(1+x,len(vNum)):
		if vNum[x] > vNum[y]:
			vNum[x],vNum[y] = vNum[y],vNum[x]
			vName[x],vName[y] = vName[y],vName[x]
print(vNum, vName)
		
	



	









