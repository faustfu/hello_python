# 1. Elements or length of elements is mutable in a list.
# 2. List could be accessd by index or slice statement.
# 3. List methods: insert, append, remove, pop, extend, index, count, sort, copy.
# 4. Use "del" statement to delete an element.
# 5. Use "in" statement to if a element is in the list.
# 6. Relative functions: sorted, len, list.
# 7. slice statement will copy from the list to make a new list.
# 8. Use iter() to turn a list into a lazy iterator.
empty_list = []
print("empty list %s" % empty_list)

some_list = [1, 3, 0, 2]
for i, x in enumerate(some_list):
    print(i, x, x * (4 ** i))

print(sum([x * (4 ** i) for i, x in enumerate(some_list)]))

print('end of i is', i)

print(iter([3, 5, 4, 1]), [3, 5, 4, 1])
