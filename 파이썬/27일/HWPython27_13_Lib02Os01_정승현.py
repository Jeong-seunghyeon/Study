import os

resultOs = os.environ

print(type(resultOs))
print(resultOs)
print('='*20)
resultPath = resultOs['PATH']
a = resultPath.split(';')
print(type(resultPath))
print(type(a))
for x in a:
	print(x)

