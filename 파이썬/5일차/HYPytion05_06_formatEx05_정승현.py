#HYPytion05_06_formatEx05_정승현.py



alignLeft = "{1:<10}".format("niceday", "hi")
print(alignLeft)


alignCenter = "{0:^10}".format("nice day")
print(alignCenter)

alignRight = "{:>10}".format("nice day")
print(alignRight)




x=342134234
y=3.42134234

floorEx1 = "{0:0.4f} {1:d}".format(y,x)
floorEx2 = "{0:10.4f}".format(y)

print(floorEx1)
print(floorEx2)


