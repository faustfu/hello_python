# 1. Dictionary is mutable.
# 2. Elements of a dictionary has no order.
# 3. Types of a key of an element includes boolean, integer, float, tuple, string and function.
# 4. Dictionary could be accessed by index statement.
# 5. Dictionary methods: update, clear, get, keys, values, items, copy.
# 6. Use "del" statement to delete an element.
# 7. Use "in" statement to if a element is in the dictionary.
empty_dict = {}
print("empty dict %s" % empty_dict)
a_dict = dict([['a', 1], ['b', 2]])
print("a dict %s" % a_dict)
b_dict = dict([('a', 1), ('b', 2)])
print("b dict %s" % b_dict)
c_dict = dict(['ab', 'cd'])
print("c dict %s" % c_dict)
d_dict = dict(('ab', 'cd'))
print("d dict %s" % d_dict)

merged = {}
merged.update(a_dict)
merged.update(c_dict)
print('merge a and c =', merged)
