# 1. There are many utilities for iterator or generator in package:itertools.
# 2. Two types could be used for declaration: typing.Sequence and typing.MutableSequence.
import itertools

MAX_ITERATION = 10

# case 1: infinite loop by a list
for i, c in enumerate(itertools.cycle('abcd')):
    print(i, c)

    if i > MAX_ITERATION:
        break

# case 2: infinite loop by a initial value with fixed interval.
for i, c in enumerate(itertools.count(5, 2)):
    print(i, c)

    if i > MAX_ITERATION:
        break

names = ['Justin', 'Monica', 'Irene', 'Pika', 'caterpillar']
for length, group in itertools.groupby(names, len):
    print(length, list(group))
