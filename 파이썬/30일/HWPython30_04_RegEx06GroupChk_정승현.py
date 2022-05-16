import re

patt = re.compile(r'\w+\s+\d+[-]\d+[-]\d+')

mapp = patt.search('park 010-1234-1234')

print(mapp)
print()
print()

patt01 = re.compile(r'\w+\s+\d+[-]\d+[-]\d+')
mapp01 = patt01.search('park 010-1234-1234')

print(mapp01.group())
print()
print()

patt02 = re.compile(r'(\w+)\s+((\d+)[-]\d+[-]\d+)')
mapp02 = patt02.search('park 010-1234-1234')


print(mapp02.group(3))
print(mapp02,'\n\n\n')

patt03 = re.compile(r'(\w)+\s+(\d+[-]\d+[-]\d+)')
mapp03 = patt03.search('park 010-1234-1234')

print(mapp03)

print(mapp03.group(2))

