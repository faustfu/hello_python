# 1. All methods are public.
# 2. Use property() to wrap a property's getter and setter.
# 3. Or use two decorators @property and @<name>.setter to indicate its getter and setter.
# 4. Cannot set a property directly if there is no setter.

class Duck():
    def __init__(self, name):
        self.hidden_name = name
    def get_name(self):
        return self.hidden_name
    def set_name(self, name):
        self.hidden_name = name
    name = property(get_name, set_name)


class Dog():
    def __init__(self, name):
        self.hidden_name = name
    @property
    def name(self):
        return self.hidden_name
    @name.setter
    def name(self, name):
        self.hidden_name = name

a = Duck('Ada')
print('Duck\'s name is', a.name)

b = Dog('Adam')
print('Dog\'s name is', b.name)
