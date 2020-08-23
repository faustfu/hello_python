# 1. Python has two scope: global or local scope.
# 2. Global variables are read-only in local scope by default.
# 3. Use "global" statement to access global variables in local scope.
# 4. Use locals() to show local variables.
# 5. Use globals() to show global variables.
a = 1


def change1():
    print('in local: ', a)


def change2():
    a = 2 # shadow the global variable by declaring it again in local scope.
    print('in local: ', a)


def change3():
    global a
    a = 2
    print('in local: ', a)


change1()
change2()

print('in global: ', a) # Global variables wouldn't be affected in local scope.


change3()

print('in global: ', a)
