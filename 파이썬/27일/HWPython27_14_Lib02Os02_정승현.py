import os


#os.system('dir')
#f = os.popen('dir')
print()
print()
#print(f.read())

os.mkdir('newDir01')
os.rmdir('newDir01')

#os.rename('test.txt','dst.txt')
os.unlink('dst.txt')




# - os.getcwd - 디렉토리 위치 돌려받기

# os.chdir 디렉토리 위치 변경하기

# os.system시스템 명령어 호출하기 

print(os.getcwd())

os.chdir('./../../')

print(os.getcwd())

