import os
import stat
import time

s = os.stat("D:\workspace\PythonAdvance\chapter3\join_test.py")
print(stat.S_ISDIR(s.st_mode))
print(stat.S_IXUSR & s.st_mode)
print(stat.S_IRUSR & s.st_mode)
print(time.localtime(s.st_atime))
print(time.localtime(s.st_ctime))
print(time.localtime(s.st_mtime))
print(s.st_size)

os.path