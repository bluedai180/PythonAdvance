from tempfile import TemporaryFile, NamedTemporaryFile

f = TemporaryFile()
f.write("adb-------------------------------".encode('utf8'))
f.seek(0)
print(f.read(10))

g = NamedTemporaryFile()
print(g.name)