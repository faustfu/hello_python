# Process operations.
# 1. Module:subprocess is for shell operations.
# 2. Module:multiprocessing is for multiple process operations.

import os
import subprocess
import multiprocessing


def do_this(what):
    whoami(what)


def whoami(what):
    print('Process %s says: %s' % (os.getpid(), what))


if __name__ == '__main__':
    print('Current pid is', os.getpid())
    print('Current script is', os.getcwd())

    subprocess.call('date')
    whoami('main')
    for n in range(4):
        p = multiprocessing.Process(target=do_this, args=('functoin %s' % n,))
        p.start()
        # p.terminate()
