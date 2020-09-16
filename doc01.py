# 1. Use ''' or """ to declare documents for packages, modules, classes or functions.
# 2. Documents for packages could be declared in __init__.py with ''' or """.
# 3. Use help(<name>) to show the document.
"""
Abstract Base Classes (ABCs) for Python Tutorial

Just a demo for DocStrings.
"""

from abc import ABCMeta, abstractmethod

class Ordering(metaclass=ABCMeta):
    '''
    A abc for implementing rich comparison methods.

    The class must define __gt__() and  __eq__() methods.
    '''
    @abstractmethod
    def __eq__(self, other):
        '''Return a == b'''
        pass

    @abstractmethod
    def __gt__(self, other):
        '''Return a > b'''
        pass

    def __ge__(self, other):
        '''Return a >= b'''
        return self > other or self == other

    def __lt__(self, other):
        '''Return a < b'''
        return not (self > other and self == other)

    def __le__(self, other):
        '''Return a <= b'''
        return (not self >= other) or self == other

    def __ne__(self, other):
        '''Return a != b'''
        return not self == other

