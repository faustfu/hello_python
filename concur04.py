from typing import Dict
from threading import Thread, Lock
import time


def set_to_1(data: Dict[str, int], lock: Lock):
    while True:
        lock.acquire()  # The thread will be blocked if it is locking.
        try:
            data['Bob'] = 1
            if data['Bob'] != 1:
                raise ValueError(f'set_to_1 concurrency error:{data}')
            print('set_to_1 is done')
        finally:
            time.sleep(1)
            lock.release()


def set_to_2(data: Dict[str, int], lock: Lock):
    while True:
        lock.acquire()  # The thread will be blocked if it is locking.
        try:
            data['Bob'] = 2
            if data['Bob'] != 2:
                raise ValueError(f'set_to_2 concurrency error:{data}')
            print('set_to_2 is done')
        finally:
            time.sleep(1)
            lock.release()


lock = Lock()
data: Dict[str, int] = {}

t1 = Thread(target=set_to_1, args=(data, lock))
t2 = Thread(target=set_to_2, args=(data, lock))

t1.start()
t2.start()
