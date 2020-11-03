# 1. Functions are objects. So they could be variables or parameters.
# 2. Functions could return new functions/closures.
# 3. Use "lambda" statement to build anonymous, one-line functions.
# 4. Use "yield" statement to build a generator function.
# 5. Use "@<decorator name>" statement before a function declaration to decorate the function.
# 6. Nearest decorator run first.


def answer():
    print("42")


def run_sth(func):
    func()


def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


def document_it(func):
    def wrapped(*args, **kwargs):
        print('running:', func.__name__)
        print('arguments:', args)
        print('keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapped

# same as document_it(add_ins), wrap a function by the decorator.
@document_it
def add_ins(a, b):
    return a + b


run_sth(answer)
run_sth(lambda: print("23"))

for i in my_range(1, 5):
    print(i)

add_ins(1, 2)
