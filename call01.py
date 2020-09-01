def inc(a: int):
    a += '1'


def push(a: list):
    a.append(1)


def add(a: int) -> callable:
    def inner(b: int) -> int:
        return a + b

    return inner


add1 = add(1)

a = '1'
inc(a)  # call by value
print(a)

b = [1]
push(b)  # call by reference
print(b)

print(add1(1))
