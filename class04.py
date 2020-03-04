# 1. Duck type: Python do type checking at runtime.
# 2. Special methods: __init__, __eq__, __ne__, __lt__, __gt__, __le__, __ge__, __str__, __len__, __repr__
# 3. Special math methods: __add__, __sub__, __mul__, __floordiv__, __truediv__, __mod__, __pow__
class Person():
  def says(self, msg):
    print(msg)

def who_says(obj, msg):
  obj.says(msg)

a = Person()

who_says(a, 'hi')
