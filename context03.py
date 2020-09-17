# 1. Use decorator:contextmanager or function:suppress to catch specified exception.

import sys
from contextlib import contextmanager, suppress
from typing import Type, Iterator

@contextmanager
def ignore(ex_type: Type[BaseException]) -> Iterator[None]: # use generator to gain control if exceptions occur.
    try:
        yield
    except ex_type: # ignore the exception
        pass

with ignore(FileNotFoundError):
    for line in open(sys.argv[1]):
        print(line, end='')

with suppress(FileNotFoundError):
    for line in open(sys.argv[1]):
        print(line, end='')
