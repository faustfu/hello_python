# 1. Use decorator:contextmanager or function:closing to call close() as leaving the block.
from contextlib import contextmanager, closing
from typing import Any, Iterator

@contextmanager
def down(thing: Any) -> Iterator[Any]:
    try:
        yield thing
    finally:
        thing.close()

class Some:
    def __init__(self, name: str) -> None:
        self.name = name

    def close(self):
        print(self.name, 'is closed.')

with down(Some('Resource')) as res:
    print(res.name)

with closing(Some('Resource')) as res:
    print(res.name)