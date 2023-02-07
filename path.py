import os, dis
print(os.path.abspath('.') + '  ' +
os.path.abspath('..\\libros')+ ' '+
os.path.relpath('C:\\Windows', 'C:\\'))
#dis.dis("os.path.abspath('.')")
#dis.dis("os.path.relpath('C:\\Windows', 'C:\\')")
