import locale

with open("out.py", "r", encoding="UTF-8") as f:
    read_data1 = f.read()
print(f.mode)
print(f.name)
print(read_data1)

f.close()
# ValueError: I/O operation on closed file.
# read_data2 = f.read()
# print(read_data2)
# print(locale.getpreferredencoding(False))
