# 1. Use timeit to test simple codes.
from timeit import timeit

prg1 = '''
all = ''
for s in strs:
  all += s + ','
all += '99'
'''

prg2 = '''
all = ','.join(strs)
'''

print('prg1 time is', timeit(prg1, 'strs = [str(n) for n in range(99)]'))

print('prg2 time is', timeit(prg2, 'strs = [str(n) for n in range(100)]'))