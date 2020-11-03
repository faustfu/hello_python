# 1. There are some useful getter in package:operator
from operator import itemgetter, attrgetter

# case 1: get by index
first = itemgetter(0)

a = [1, 2, 3]
b = '456'
c = (7, 8, 9)

first = itemgetter(0)

print(first(a), first(b), first(c))

# case 2: get class property
get_name = attrgetter('name')

class Customer:
    def __init__(self, name, symbol, age):
        self.name = name
        self.symbol = symbol
        self.age = age

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return "Customer('{name}', '{symbol}', {age})".format(**vars(self))

    def __repr__(self):
        return self.__str__()

customers = [
    Customer('Justin', 'A', 40),
    Customer('Irene', 'C', 8),
    Customer('Monica', 'B', 37)
]

for customer in customers:
  print(get_name(customer))