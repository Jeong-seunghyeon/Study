

import re

vData = '''
http://google.com
http://google.bar
http://google.bat
http://google.exe
http://google.cf
http://google.c
http://google.jpg
'''

patt01 = re.compile(".*[.].*$", re.M)
patt02 = re.compile(".*[.][^b].*$", re.M)
patt03 = re.compile(".*[.]([^b]..|.[^a].|..[^t])$", re.M)###
patt03_1 = re.compile(".*[.][^b]..$|.*[.].[^a].$|.*[.]..[^t]$", re.M)
patt04 = re.compile(".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$", re.M)

patt05 = re.compile(".*[.](?!bat$)", re.M)
patt06 = re.compile(".*[.](?!bat$).$", re.M)
patt07 = re.compile(".*[.](?!bat$).*$", re.M)
patt08 = re.compile(".*[.](?!bat$|exe$).*$", re.M)

mapp01 = patt01.findall(vData)
print(mapp01,"\n\n")
mapp01 = patt02.findall(vData)
print(mapp01,"\n\n")
mapp01 = patt03.findall(vData)
print(mapp01,"\n\n")
mapp01 = patt03_1.findall(vData)
print(mapp01,"\n\n")
mapp01 = patt04.findall(vData)
print(mapp01,"\n\n")
mapp01 = patt05.findall(vData)
print(mapp01,"\n\n")
mapp01 = patt06.findall(vData)
print(mapp01,"\n\n")
mapp01 = patt07.findall(vData)
print(mapp01,"\n\n")
mapp01 = patt08.findall(vData)
print(mapp01,"\n\n")