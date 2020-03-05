# 1. A byte is range from 0 to 255.
# 2. Class:bytes is immutable. Class:bytearray is mutable.
# 3. Module:struct is for converting bytes.
import struct

blist = [1,2,3,255]

a_bytes = bytes(blist)
print(a_bytes)

a_byte_array = bytearray(blist)
print(a_byte_array)

print(struct.unpack('<H', b'\x01\x02'))
print(struct.unpack('>H', b'\x01\x02'))
print(struct.pack('<H', 258))
print(struct.pack('>H', 258))

print(struct.unpack('<2B', b'\x01\x02'))
print(struct.unpack('>2B', b'\x01\x02'))

print(struct.unpack('<1xB', b'\x01\x02'))
print(struct.unpack('>1xB', b'\x01\x02'))
