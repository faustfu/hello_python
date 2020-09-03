# 1. Use "class" statement to define a class.
# 2. Use "__init__" method to define the constructor.
# 3. Methods include object method, class method and static method.
# 4. First paremeter of object/class methods is its object/class reference.
# 5. Use "self/cls" for naming the object/class reference.
# 6. Methods' default type is object method.
# 7. Use "@classmethod" before the method to indicate that is a class method.
# 8. Use "@staticmethod" before the method to indicate that is a static method.
# 9. Class method and static method could be accessed directly by the class.
class Person1():
  pass

class Person2():
  def __init__(self, name):
    self.name = name # property of instance

class Person3():
  count = 0 # property of class

  def __init__(self):
    Person3.count += 1

  def exclaim(self):
    pass

  @classmethod
  def kids(cls):
    print('Person3 has', cls.count, 'objects.')

a = Person1()
print(a)

b = Person2('b')
print('I am', b.name)

c1 = Person3()
c2 = Person3()
c3 = Person3()
Person3.kids()