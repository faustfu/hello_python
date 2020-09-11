# 1. A byte is range from 0 to 255.
# 2. Class:bytes is immutable. Class:bytearray is mutable.
# 3. Module:struct is for converting bytes.
# 4. Module:binascii is for converting base 16/64...
# 5. Byte operators: &, |, ^, ~, <<, >>

import struct
import binascii

blist1 = [1, 2, 3, 255]
print('raw list =', blist1)
a_bytes = bytes(blist1)
print('bytes([1, 2, 3, 255]) =', a_bytes)

a_byte_array = bytearray(blist1)
print('bytearray[1, 2, 3, 255] =', a_byte_array)

print(r"struct.unpack('<H', b'\x01\x02') =", struct.unpack('<H', b'\x01\x02'))
print(r"struct.unpack('>H', b'\x01\x02') =", struct.unpack('>H', b'\x01\x02'))
print(r"struct.pack('<H', 258) =", struct.pack('<H', 258))
print(r"struct.pack('>H', 258) =", struct.pack('>H', 258))

print(r"struct.unpack('<2B', b'\x01\x02') =",
      struct.unpack('<2B', b'\x01\x02'))
print(r"struct.unpack('>2B', b'\x01\x02') =",
      struct.unpack('>2B', b'\x01\x02'))

print(r"struct.unpack('<1xB', b'\x01\x02') =",
      struct.unpack('<1xB', b'\x01\x02'))
print(r"struct.unpack('>1xB', b'\x01\x02') =",
      struct.unpack('>1xB', b'\x01\x02'))

blist2 = [1, 38, 50, 255]
b_bytes = bytes(blist2)
print('raw bytes =', b_bytes)
print('binascii.hexlify =', binascii.hexlify(b_bytes))
print(r"binascii.unhexlify(b'012632ff') =", binascii.unhexlify(b'012632ff'))

print(r"100 & 200 =", 100 & 200)  # byte calculation
