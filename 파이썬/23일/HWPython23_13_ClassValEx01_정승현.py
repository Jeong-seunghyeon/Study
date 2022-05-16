'''
01. CalssValChk 클래스 생성
		-vI = 10 # 메소드 외부, 클래스 내부
		-mv01 = 10 # 생성자에 의해 초기화
02. obj01 = ClassValChk()
	obj02 = ClassValChk()
	obg03 = ClassValChk()
obj01.mv01 += 10 # 20
obj01.vl      += 10 # 20
'''

class ClassValChk:
	vI = 10
	mv01 = 10
	
		

obj01 = ClassValChk()
obj02 = ClassValChk()
obj03 = ClassValChk()

obj01.mv01 += 10
print(obj01.mv01)
ClassValChk.vI+=10
print(obj01.vI,ClassValChk.vI)

obj02.mv01 += 10
print(obj02.mv01)
ClassValChk.vI += 10
print(obj02.vI,ClassValChk.vI)


obj03.mv01 += 10
print(obj03.mv01)
ClassValChk.vI += 10
print(obj03.vI, ClassValChk.vI)

