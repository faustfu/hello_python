# Use threads.
import threading


def do_this(what):
    whoami(what)


def whoami(what):
    print('Thread %s says: %s' % (threading.current_thread(), what))


if __name__ == '__main__':
    whoami('hi')

    for n in range(4):
        p = threading.Thread(target=do_this, args=('func %s' % n,)) # create a thread to do a task.
        p.start()
