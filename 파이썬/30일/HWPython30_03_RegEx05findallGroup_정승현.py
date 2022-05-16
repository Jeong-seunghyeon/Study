import re

patt = re.compile('[a-z]+')

result = patt.findall('life is too short 3 Exam Nice')

print(result)


patt01 = re.compile('[a-z]+')

result01 = patt01.finditer('life is too short')
print(result01)

for r in result01:
	print(r)
	print(r.group())

patt02 = re.compile('[a-z]+')

mapp = patt02.match('have a nice day')

print(mapp.group())
print(mapp.start())
print(mapp.end())
print(mapp.span())
