# 1. Use typing.Iterator to limit the type of iterators.
from typing import Iterator


def iter_primes() -> Iterator[int]: # return an int iterator
    return [1, 2, 3]


for i in iter_primes():
    print(i)
