# 1. String could be processed as a unicode character list.
# 2. Use actual characters, "\uXXXX", "\UXXXXXXXX", "\N{<charccter name>}" to assign unicode characters.
# 3. len() will calculate unicode character number.
# 4. String provides a method:encode() to convert to a byte string.
# 5. String provides a method:decode() to convert from a byte string.
a = "a一b二"
for c in a:
  print(c)

b = 'caf\u00e9'
c = 'café'
d = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(b, c, d)

bb = b.encode('ascii', 'replace')
be = bb.decode('ascii')
print(b, bb, be)
