import re

patt01 = re.compile('[0-9]')
patt01_1 = re.compile(r'\d')
patt02 = re.compile('[a-zA-Z0-9]')
patt02_1 = re.compile(r'\w')
patt03 = re.compile('[\t\n\r\f\v]')
patt03_1 = re.compile(r'\s')

print(patt01.match('Abcd34'))
print(patt01_1.match('Abcd34'))
print(patt01.match('34'))
print(patt01_1.match('34'))
print()
print()

print(patt02.match('Abcd34'))
print(patt02.match('34'))
print(patt02_1.match('Abcd34'))
print(patt02_1.match('34'))

print()

print()
print(patt03.match('Abcd34'))
print(patt03.match('34'))
print(patt03.match('										'))
print(patt03_1.match('Abcd34'))
print(patt03_1.match('34'))
print(patt03_1.match('			'))



