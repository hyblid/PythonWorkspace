import glob
from pathlib import Path
"""
print('Named explicitly:')
for name in glob.glob('/home/geeks/Desktop/gfg/data.txt'):
    print(name)
1. for name in open('C:\\test\\PythonWorkspace\\sample.txt'):
2. for name in open(r'C:\test\PythonWorkspace\sample.txt'):
3. for name in open('C:/test/PythonWorkspace/sample.txt'):
4. if cwd is project director 
   for name in open(".\\txt_files\\pg345.txt"):
   for name in open(r".\txt_files\pg345.txt"):
   for name in open("./txt_files/pg345.txt"):
"""
print('Named explicitly:')
for name in open("./txt_files/pg345.txt"):
    print(name)
