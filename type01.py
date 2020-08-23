from typing import Iterator


def iter_primes() -> Iterator[int]:
    return [1, 2, 3]


for i in iter_primes():
    print(i)
