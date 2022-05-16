import re

patt = re.compile('(blue|white|red)')
mapp = patt.sub('color', 'blue socks and red shoes')

print(mapp)

patt01 = re.compile('(blue|white|red)')
mapp01 = patt01.subn('color', 'blue socks and red shoes')
print(mapp01)

patt02 = re.compile('(blue|white|red)')
mapp02 = patt02.sub('color', 'blue socks and red shoes', count=1)
print(mapp02)

patt03 = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
print(patt03.sub('\g<phone> \g<name>', 'park 010-1234-1234'))

patt04 = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
print(patt04.sub('\g<2> \g<1>', 'park 010-1234-1234'))





