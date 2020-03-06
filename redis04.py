import redis

conn = redis.Redis()

# access a set
conn.sadd('inventory', 'sword', 'shield', 'armor')  # set properties
print(conn.scard('inventory'))  # get property number
print(conn.smembers('inventory')) # get all properties
conn.srem('inventory','armor') # remove a property
print(conn.smembers('inventory'))

conn.sadd('loot', 'sword', 'hat', 'robe')
print(conn.smembers('loot'))

print(conn.sinter('inventory', 'loot')) # get intersection of two sets
print(conn.sunion('inventory', 'loot')) # get union of two sets
print(conn.sdiff('loot', 'inventory')) # get sth that is in loot but not in inventory.

conn.srem('inventory', 'sword', 'shield', 'armor')
conn.srem('loot', 'sword', 'hat', 'robe')
