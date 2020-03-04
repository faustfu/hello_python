# 1. Use "class" statement to define an object type.
# 2. Use "__init__" method to define the constructor.
class Person1():
  pass

class Person2():
  def __init__(self, name):
    self.name = name

a = Person1()
print(a)

b = Person2('b')
print('I am', b.name)