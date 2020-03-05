filename = 'bfile.out'

bdata = bytes(range(0, 256))

fout = open(filename, 'wb')  # open binary file to write.
fout.write(bdata)
fout.close()

fin = open(filename, 'rb')
bdata = fin.read()
fin.close()
print(bdata)

fin = open(filename, 'rb')
print(fin.read(20))
print(fin.tell())  # tell() return current position.
print(fin.seek(30))  # seek() move to new position.
print(fin.seek(1, 1))  # move to next byte.
print(fin.seek(-1, 2))  # move to the final byte.
fin.close()
