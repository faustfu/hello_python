# 1. Use streams to suopport multiple consumers.

import redis

sample = {
    "sensor-id": 1234, "temperature": 19.8
}

name = "mystream"

conn = redis.Redis()

# get stream length.
print(conn.xlen(name))

# for i in range(1):
#     # append to the stream and generate new id systematically.
#     conn.xadd(name, sample)

# query streams by its name and id pattern.
print(conn.xread({name: '0-0'}))

# # wait for a new entry to be appended.
# print(conn.xread({name: '$'},block=0))

# # query streams by its name and id range from the smallest to the greatest.
# print(conn.xrange(name, min='-', max='+'))

# # get the newest streams.
# print(conn.xrevrange(name, max='+', min='-', count=1))
