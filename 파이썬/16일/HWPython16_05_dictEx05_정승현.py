#HWPython16_05_dictEx05_정승현.py

myfamily = {
	"child1" : {
		"name" : "Totti",
		"year" : 2004
		},
	"child2" : {
		"name" : "zeko",
		"year" : 2006
		},
	"child3" : {
		"name" : "de losi",
		"year" : 2008
		}
	}

child1 = {
		"name" : "Totti",
		"year" : 2004
}
child2 = {
		"name" : "zeko",
		"year" : 2006
		}
child3 = {
		"name" : "de losi",
		"year" : 2008
		}

myfamily = {
	"child1" : child1,
	"child2" : child2,
	"child3" : child3
}

print(myfamily)