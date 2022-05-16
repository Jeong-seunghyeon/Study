import re

patt01 = re.compile('a.b')
print(patt01.match('aab'))
print(patt01.match('a0b'))
print(patt01.match('a000b'))
print(patt01.match('abc'))

patt02 = re.compile('ca*t')

print(patt02.match('ct'))
print(patt02.match('cat'))
print(patt02.match('caaat'))


patt03 = re.compile('ca+t')

print(patt03.match('ct'))
print(patt03.match('cat'))
print(patt03.match('caaat'))
