# 1. Use "yield" to simulate a sync channel with only one capacity.
import sys
import random


def producer():
    while True:
        data = random.randint(0, 9)
        print(f'createed: {data}')
        yield data  # pass the data and wait for next step


def consumer():
    while True:
        data = yield  # wait for the data to do next step
        print(f'got: {data}')


def channel(rounds, producer, consumer):
    print((f'Total rounds: {rounds}'))
    p = producer()
    c = consumer()
    next(c)  # block the consumer
    for _ in range(rounds):
        data = next(p)
        c.send(data)


channel(int(sys.argv[1]), producer, consumer)
