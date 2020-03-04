# 1. Inheritance is a way to reuse codes.
# 2. Subclass could replace superclass's methods or create new methods.
# 3. Subclass could use super() to get superclass's object reference.
class Car():
    def __init__(self, name):
        self.name = name

    def exclaim(self):
        print('I am a car.')


class Yugo(Car):  # Yugo is a Car.
    def exclaim(self):
        print('I am a yugo with a name "%s".' % self.name)


Yugo('b').exclaim()
