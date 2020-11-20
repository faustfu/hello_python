# 1. There are many utilities for iterator or generator in package:itertools.
# 2. Two types could be used for declaration: typing.Sequence and typing.MutableSequence.
import itertools as it

MAX_ITERATION = 10

# case 1: infinite loop by a list
for i, c in enumerate(it.cycle('abcd')):
    print(i, c)

    if i > MAX_ITERATION:
        break

# case 2: infinite loop by a initial value with fixed interval.
for i, c in enumerate(it.count(5, 2)):
    print(i, c)

    if i > MAX_ITERATION:
        break

# case 3: group elements by a specified rule into a finite iterator.
names = ['Justin', 'Monica', 'Irene', 'Pika', 'caterpillar']
for length, group in it.groupby(names, len):
    print(length, list(group))

# case 4: join some sets into a finite iterator.
chain = it.chain([1, 2, 3], ['a', 'b', 'c'], ['End'])
for i in chain:
    print(i)

# case 5: bypass sth until the condition is ok and do remains.
jobs = ['job1', 'job2', 'job3', 'job10', 'job4', 'job5']
dropwhile = it.dropwhile(lambda x: len(x) == 4, jobs)
for i in dropwhile:
    print(i)

# case 6: do sth until the condition is ok.
jobs = ['job1', 'job2', 'job3', 'job10', 'job4', 'job5']
takewhile = it.takewhile(lambda x: len(x) == 4, jobs)
for i in takewhile:
    print(i)

# case 7: split + loop
iterable = '日一二三四五六'
tee = it.tee(iterable, 4)
for i in tee:
    print(list(i))

# case 8: generate possible different sets.(排列)
iterable = 'FM1'
permutations = it.permutations(iterable)
for i in permutations:
    print(i)

# case 8: generate possible different combinations.(組合)
iterable = 'AB1'
combinations = it.combinations(iterable, 2)
for i in combinations:
    print(i)