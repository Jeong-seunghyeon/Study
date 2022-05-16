#HWPython11_03_SelectSortFinish_정승현.py



'''
outer loop
시작 : index 0 
종료 : len - 1

inner loop
시작 : outer + 1
종료 : len
'''


a = [75,65,100,80,90,55,95,30,20,50]
asc_a=[]
#a1 = outer  len -1
#a2 = inner   len

print('변경전',a)


print('과정')
'''
for a1 in range(len(a)-1):
	for a2 in range(a1+1,len(a)):
		if a[a1] < a[a2]:
			a[a1],a[a2] = a[a2],a[a1]
			print(a)
내림차순
'''



for a1 in range(len(a)-1):
	for a2 in range(a1+1,len(a)):
		if a[a1] > a[a2]:
			a[a1],a[a2] = a[a2],a[a1]
			print(a)


print('변경 후')
print(a)


			

		

