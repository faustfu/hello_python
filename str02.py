# 1. Use "<format string> % data/tuple" to format string output.

# python2
print('%s%%' % 42)
print('%x' % 42)
print('%f %e %g' % (7.123, 7.123, 7.123))
print('[%10s] [%-10s]' % ('hello', 'world'))
print('[%10.4s] [%-10.4s]' % ('hello', 'world'))
print('[%*.*s] [%*.*s]' % (10, 4, 'hello', -10, 4, 'world'))

# python3
print('{} {} {}'.format(4.123, 5.123, 6.123))
print('{2} {0} {1}'.format(4.123, 5.123, 6.123))
print('{a} {b} {c}'.format(c=4.123, b=5.123, a=6.123))
d = {'a': 4.123, 'b': 5.123, 'c': 6.123}
print('{0[a]} {0[b]} {1}'.format(d, 'more'))
print('{0:f} {1:e} {2:g}'.format(4.123, 5.123, 6.123))
print('{a:f} {b:e} {c:g}'.format(c=4.123, b=5.123, a=6.123))
print('[{a:10f}] [{b:-10e}] [{c:10g}]'.format(c=4.123, b=5.123, a=6.123))
print('[{0:>10.4f}] [{1:<10.4e}] [{2:^10.4g}]'.format(4.123, 5.123, 6.123))
