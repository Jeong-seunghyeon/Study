#HWPython23_10_InheritEx01_정승현.py

# 조건 ) 01. InheritParent 클래스 생성. vI01 = 20 # MV 생성자 초기화
#          02. mView() 부모메소드 확인 print(부모메소드 확인)
#          03. InheritChild 클래스 생성 << InheritParent(상속)
#          04. mView() override . print(' 자식메소드 확인')
#          05. obj = InheritChild()
#				 obj.vI01 = 20
#				 obj.mView() = 자식 메소드 확인


class InheritParent:
	vI01 = 20
	def __init__(self):
		self.vI01 =20 
	def mView(self):
		print('부모메소드 확인')
	
class InheritChild(InheritParent):
	def mView(self):
		super().mView()
		print('자식메소드 확인')

obj = InheritChild()
print(obj.vI01)
obj.mView()
