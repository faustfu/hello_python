import os
import shutil
import glob

filename = 'oops.txt'
newname = 'ohno.txt'
tmpname1 = 'ohyes.txt'
tmpname2 = 'ohya.txt'
linkname = 'qoos.txt'
slinkname = 'waha.txt'
foldername = 'dump'

with open(filename, 'wt') as fout:
    fout.write('BACD\ndges\tpslsss')

if os.path.exists(filename):
    print(filename, 'exists!')
else:
    raise Exception('huh?')

print(os.path.abspath(filename))
print('is file?', os.path.isfile(filename))
print('is directory?', os.path.isdir(filename))
print('is absolutely path?', os.path.isabs(filename))

shutil.copy(filename, newname)
shutil.move(newname, tmpname1)

os.rename(tmpname1, tmpname2)

os.remove(tmpname2)

os.mkdir(foldername)

if os.path.exists(foldername):
    print(foldername, 'exists!')
else:
    raise Exception('huh?')

os.chdir(foldername)
print(os.listdir('.'))

os.chdir('..')
os.rmdir(foldername)

print(glob.glob('*.txt'))