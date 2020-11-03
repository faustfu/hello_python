from os03 import root
import os

# print('lv = 21', __file__)
# print('lv = 21', os.path.abspath(__file__))
# print('lv = 21', os.path.realpath(__file__))

print('root =', root)
print('seperator =', os.path.sep)
print('relative path =', os.path.relpath(__file__, root))

namespace = os.path.relpath(__file__, root)#.replace(os.path.sep, '_')
file = os.path.splitext(namespace)[0]
print(file.replace(os.path.sep, '_'))
