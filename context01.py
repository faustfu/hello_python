# 1. Use statement "with as" to release automatically.
from types import TracebackType
from typing import Optional, Type


class Resource:
    def __init__(self, name: str) -> None:
        self.name = name

    def __enter__(self):
        print(self.name, ' __enter__')

        return self # return self object.

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> Optional[bool]:
        print(self.name, ' __exit__')

        return False # return False to popup exceptions.


with Resource('res') as resource:
    print(resource.name)
