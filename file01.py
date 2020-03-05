# 1. open mode: r(read-only), w(write), x(write if not exists), t(text), b(binary)
# 2. Use "with" statement to close file automatically.

filename = 'poem.txt'
poem = '''abc
def
一二三'''
print(poem)

fout = open(filename, 'wt')
fout.write(poem)  # another way: print(poem, file=fout, sep='', end='')
fout.close()

fin = open(filename, 'rt')
print(fin.read())
fin.close()

fin = open(filename, 'rt')
chunk = 1
poem = ''
while True:
    fragment = fin.read(chunk)  # read fixed number of characters.
    if not fragment:
        break
    poem += fragment
    print(fragment)
fin.close()

fin = open(filename, 'rt')
poem = ''
while True:
    line = fin.readline()  # read a line.
    if not line:
        break
    poem += line
    print(line, end='')
fin.close()
print()

fin = open(filename, 'rt')
lines = fin.readlines()  # read all by lines.
fin.close()
for line in lines:
    print(line, end='')
print()

with open(filename, 'wt') as fout:
    fout.write(poem)
