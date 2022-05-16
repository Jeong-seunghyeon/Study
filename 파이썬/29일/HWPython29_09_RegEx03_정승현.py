import re

patt01 = re.compile('ca{2}t')

print(patt01.match('cat'))
print(patt01.match('caat'),'\n\n\n')


patt02 = re.compile('ca{2,5}t')

print(patt02.match('cat'))
print(patt02.match('caat'))
print(patt02.match('caaaat'))
print(patt02.match('caaaaaat'),'\n\n\n')


patt03 = re.compile('ab?c')

print(patt03.match('abc'))
print(patt03.match('ac'))
print(patt03.match('abbc'))
print()
print()

patt04 = re.compile('ca{2,}')

print(patt04.match('cat'))
print(patt04.match('caat'))
print(patt04.match('ca'))
print(patt04.match('caaaaaaat'))

print()
print()
print()
patt05 = re.compile('ca{,5}')

print(patt05.match('ca'))
print(patt05.match('cat'))
print(patt05.match('caat'))
print(patt05.match('caaaat'))
