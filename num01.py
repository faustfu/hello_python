import numpy as np
from numpy import *

print(np.array([1, 2, 3, 4]))  # create an array
print(np.arange(10))  # create an array in range
print(np.arange(1, 5, 2))  # create an array in range
# create an array of float point number in range
print(np.arange(1.2, 5.4, 1.4))
# create an array of integer number in range
print(np.arange(1.2, 5.4, 1.4, dtype=np.int))

a = np.arange(1.2, 5.4, 1.4, dtype=np.int)
print(a.ndim)  # get dimension of the array
print(a.size)  # get total size of the array
print(a.shape)  # get shape of dimension of the array

print(np.zeros((2, 4)))  # create an array in shape.
print(np.ones((2, 4)))  # create an array of '1' in shape.
print(np.random.random((2, 4)))  # create an array of random number in shape.

# create a new array by old array elements and new shape.
b = a.reshape((2, 2))
print(b)
print(b[1, 0])  # access by location
print(b[1, :])  # access by slice

print(b * 3) # do operation with all elements
