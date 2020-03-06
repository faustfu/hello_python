import redis

conn = redis.Redis()

# access a list
conn.lpush('zoo', 'bear', 'duck') # push a value from left into the list
print(conn.lrange('zoo', 0, -1)) # get the list
conn.lset('zoo', 1, 'cat')
print(conn.lrange('zoo', 0, -1))
conn.rpush('zoo', 'rabbit', 'rat') # push a value from right into the list
print(conn.lrange('zoo', 0, -1))
print(conn.lindex('zoo', 1)) # get a value by index
conn.delete('zoo')
