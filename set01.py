# 1. Set is like a dictionary without values.
# 2. Elements of a set could not be duplicated.
# 3. Use "in" statement to if a element is in the set.
# 4. Use "&", "|",  "-", "^" operators with another set to get the intersection, union, difference, symmetric difference.
# 5. Use "<=", "<", ">=", ">" operators with another set to examine the relation.
# 6. Set methods: intersection, union, difference, symmetric_difference, issubset, issuperset.
empty_set = set()
print("empty set %s" % empty_set)
a_set = {1,2,3,4}
print("a set %s" % a_set)
b_set = set('letters')
print("b set %s" % b_set)
c_set = set({'a':1, 'b': 2})
print("c set %s" % c_set)
