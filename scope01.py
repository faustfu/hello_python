# 1. Python has two scope: global or local scope.
# 2. Global variables are read-only in local scope by default.
# 3. Use "global" statement to access global variables in local scope.
# 4. Use locals() to show local variables.
# 5. Use globals() to show global variables.
a = 1


def change1():
    print('in local: ', a)


def change2():
    a = 2
    print('in local: ', a)


def change3():
    global a
    a = 2
    print('in local: ', a)


change1()
change2()

print('in global: ', a)


change3()

print('in global: ', a)
