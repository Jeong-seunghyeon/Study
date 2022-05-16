f1 = open('파일생성하기연습.txt','r')
line = f1.readline()
print(line)
f1.close()
print()


f2 = open('파일생성하기연습.txt','r')
while True:
	line = f2.readline()
	if not line: break
	print(line,end='')
f2.close

