#HWPython04_02_printEx01_정승현.py

money = int(input("money를 입력:"))
card = eval(input("True 또는 False 입력.:"))

if money >= 3000 or card:
	print("택시를 타고가라01", end ='\t')
	print("택시를 타고가라02")
else:
	print("걸어가라")


