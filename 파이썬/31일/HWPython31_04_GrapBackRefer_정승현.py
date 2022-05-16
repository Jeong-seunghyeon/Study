import re

patt = re.compile(r'(\b\w+)\s+\1')

patt2 = re.compile(r'(\b\w+)+s+')

print(patt.search('Paris in the spring spring'))
print(patt2.search('Paris in the2 the1 spring'))
