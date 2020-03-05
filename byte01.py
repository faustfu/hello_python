# 1. A byte is range from 0 to 255.
# 2. Class:bytes is immutable. Class:bytearray is mutable.
# 3. Module:struct is for converting bytes.
# 4. Module:binascii is for converting base 16/64...
# 5. Byte operators: &, |, ^, ~, <<, >>

import struct
import binascii

blist1 = [1,2,3,255]

a_bytes = bytes(blist1)
print(a_bytes)

a_byte_array = bytearray(blist1)
print(a_byte_array)

print(struct.unpack('<H', b'\x01\x02'))
print(struct.unpack('>H', b'\x01\x02'))
print(struct.pack('<H', 258))
print(struct.pack('>H', 258))

print(struct.unpack('<2B', b'\x01\x02'))
print(struct.unpack('>2B', b'\x01\x02'))

print(struct.unpack('<1xB', b'\x01\x02'))
print(struct.unpack('>1xB', b'\x01\x02'))

blist2 = [1,38,50,255]
b_bytes = bytes(blist2)
print(b_bytes)
print(binascii.hexlify(b_bytes))
print(binascii.unhexlify(b'012632ff'))

print(100 & 200) # byte calculation
