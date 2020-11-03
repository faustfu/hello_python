# 1. Using named tuples to collect relative data is easier than using classes.
# 2. Data inside a named tuple could be accessed by its name.
# 3. Named tuples is immutable. But it could be cloned with new data.
from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')

# initial by parameter order
duck1 = Duck('orange', 'long')
print(duck1)

# initial by parameter name
duck2 = Duck(bill='red', tail='long')
print(duck2)

# initial by a dict
adict = {'bill': 'black', 'tail': 'very long'}
duck3 = Duck(**adict)
print(duck3)

print('duck1 bill is', duck1.bill, ', duck2 bill is',
      duck2.bill, ', duck3 bill is', duck3.bill)

# initial by another tuple
duck4 = duck3._replace(tail='short')
print(duck4)

# initial by a list
alist = ['gogo', 'duck']
duck5 = Duck(*alist)
print(duck5)

# show by values
for v in duck5:
    print(v)

# show by pairs
for k,v in duck5._asdict().items():
    print(k,v)
