#demoRandomOS.py



from os.path import *
from os import *
import glob

print(abspath("python.exe"))
print(basename("c:\\python310\python.exe"))

if exists("c:\\python310\\python.exe"):
    print("파일크기:{0}".format(getsize("c:\\python310\\python.exe")))
else:
          print("파일이 없음")

print("운영체제이름:{0}".format(name))
print("환경변수:{0}".format(environ))
#system("notepad.exe")

#파일 목록
import glob
result = glob.glob("c:\\work\\*.py")
for item in result:
    print(item)