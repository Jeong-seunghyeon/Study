#HWPython08_02_EmployeeV00Step01_정승현.py


TName = ["구분","사원명","입사일","급여"]

empInfo = [
	['T160501',"캔디","2016-05-10"],
	['R160510',"장미","2016-05-10"],
	['t160811',"튤립","2016-08-15"],
	['T160821',"포도","2016-08-22"],
	['r160850',"사과","2016-08-30"]
]

empPayTable = [
	[250,10],
	[200,12],
	[300,9],
	[230,11],
	[150,12]
]

for x in range(len(TName)):
	print('\t  ',TName[x],'\t\t',end="      ")
print()
print('='*120)


for i in range(len(empInfo)):

	if (empInfo[i][0][0].upper())=='T':
		print('\t',"계약직 \t" ,'\t\t', empInfo[i][1] ,'\t\t                ', empInfo[i][2] ,'\t                  ', (empPayTable[i][0]*empPayTable[0][1]))
	elif(empInfo[i][0][0].upper())=='R':
		print('\t',"정규직 \t" ,'\t\t', empInfo[i][1] ,'\t\t                ', empInfo[i][2] ,'\t                  ', (empPayTable[i][0]*empPayTable[0][1]))
	


	















