# Use decorator:contextmanager to clear resources.
import sys
from contextlib import contextmanager
from typing import Iterator, IO

@contextmanager
def file_reader(filename) -> Iterator[IO]:
    try:
        f = open(filename, 'r')
        yield f # yield sth
    finally:
        f.close() # clear sth

with file_reader(sys.argv[1]) as f:
    for line in f:
        print(line, end='')
