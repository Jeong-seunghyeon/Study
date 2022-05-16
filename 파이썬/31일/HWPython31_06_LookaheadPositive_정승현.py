import re

patt = re.compile('.+.')
mapp = patt.search('http://google.com')
print(mapp.group())

patt01 = re.compile('.+(?=:)')
m = patt01.search('http://google.com')
print(m.group())

