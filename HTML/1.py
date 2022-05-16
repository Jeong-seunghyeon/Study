import re

patt01 = re.compile("^python\s\w+",re.MULTILINE)
patt02 = re.compile("^Apython\s\w+",re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(patt01.findall(data),'\n\n\n')
print(patt02.findall(data),'\n\n\n')

patt = re.compile(r'\bclass\b')

print(patt.search('no class at all'))

print(patt.search('the declassified algorithm'))



