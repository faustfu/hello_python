import redis

conn = redis.Redis()

# access a hash/map
conn.hmset('dic', {'a': 1, 'b': 2})  # set properties
conn.hset('dic', 'c', 3)  # set a property

print(conn.hget('dic', 'c'))  # get a property
print(conn.hmget('dic', 'b', 'a'))  # get properties

conn.hsetnx('dic', 'd', 4)  # set a property if not exists

print(conn.hkeys('dic'))  # get keys
print(conn.hvals('dic'))  # get values
print(conn.hlen('dic'))  # get property number
print(conn.hgetall('dic'))  # get all hash
