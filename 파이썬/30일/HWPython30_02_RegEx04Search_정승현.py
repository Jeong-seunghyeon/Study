import re

patt = re.compile('[a-z]+')

mapp = patt.match('have a nice day')
print(mapp,'\n\n\n')

mapp = patt.match('3 python')
print(mapp,'\n\n\n')


patt01 = re.compile('[a-z]+')

mapp = patt01.match('string goes here')

if mapp:
	print('Match found: ',mapp.group())
else:
	print('No match')


patt02 = re.compile('[a-z]+')

mapp = patt02.match('have a nice day')
print(mapp,'\n\n\n')

mapp = patt02.match('3 have a nice day')
print(mapp,'\n\n\n')

mapp = patt02.search('have a nice day')
print(mapp,'\n\n\n')

mapp = patt02.search('3 have a nice day')
print(mapp,'\n\n\n')

