# 1. Use class-level properties to do singleton.
from typing import Dict, Type

TLogger = Type['Logger']


class Logger:
    __loggers: Dict[str, TLogger] = {}

    def __new__(cls: TLogger, name: str) -> TLogger:
        if name not in cls.__loggers:
            logger = object.__new__(cls)

            # register the new object into the class.
            cls.__loggers[name] = logger

            return logger

        # return the registered obj to avoid creating it again.
        return cls.__loggers[name]

    def __init__(self, name: str) -> None:
        # assign that name to the object if it is new.
        if 'name' not in vars(self):
            self.name = name

    def log(self, message: str):
        print(f'{self.name}: {message}')

test_1 = Logger('test')
test_1.log('hi from test 1')

test_2 = Logger('test')
test_2.log('hi from test 2')