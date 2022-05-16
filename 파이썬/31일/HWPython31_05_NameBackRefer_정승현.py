import re

p = re.compile(r'(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)')

m = p.search('park 010-1234-1234')

print(m.group('name'))

p1 = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')

print(p1.search('Paris in in the the spring').group())

