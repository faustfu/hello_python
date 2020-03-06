import redis
import time

now = time.time()
conn = redis.Redis()

# access a ordered set
conn.zadd('logins', {'user01': now})  # add a pair
conn.zadd('logins', {'user03': now+(2*60*60)})
conn.zadd('logins', {'user02': now+(5*60)})
conn.zadd('logins', {'user01': now+(24*60*60)})  # update a pair's score

print(conn.zrange('logins', 0, -1))  # get all keys
print(conn.zrank('logins', 'user01')+1)  # get a pair's rank by score
print(conn.zscore('logins', 'user01'))  # get a pair's score
print(conn.zrange('logins', 0, -1, withscores=True))  # get all pairs
