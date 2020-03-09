# 1. Use vars() to get arguments of the function.
# 2. Use decorators to get arguments and output of the function.
# 3. Use "python -m pdb <python scrupt>..." to start debugger.
#    "b": show all breakpoints.
#    "b <line number>": create a breakpoint at the line.
#    "s": run a line of codes.
#    "n": run a line of codes but skip functions.
#    "c": run to any breakpoints or the end.
#    "p <statement>": show statement value.
#    "l <number>": show followed lines of codes.
#    "q": quit the debugger.

def func1(*args, **kwargs):
    print(vars())


def dump(func):
    'Print input arguments and output value(s)'
    def wrapped(*args, **kwargs):
        print('Function name: %s' % func.__name__)
        print('Input arguments: %s' % ' '.join(map(str, args)))
        print('Input keyword arguments: %s' % kwargs.items())
        output = func(*args, **kwargs)
        print('Output:', output)
        return output
    return wrapped


@dump # decorators will be called before the function
def func2(*args, **kwargs):
    pass


func1(1, 2)
func2(3, 4)
