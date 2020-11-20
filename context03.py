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

@contextmanager
def catch(msg: str = '', sub_title: str = '', title: str = '') -> Iterator[None]:
    try:
        yield
    except Exception as e:
        print(f'{title}{sub_title})Unknown error {e}, msg = {msg}')

with catch():
    print('ok')
    raise Exception('Huh?')
