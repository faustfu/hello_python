# Use redis to build pubsub mode.
# server
import redis
import random

conn = redis.Redis()
cats = ['cat 1', 'cat 2', 'cat 3', 'cat 4', 'cat 5']
hats = ['hat 1', 'hat 2', 'hat 3', 'hat 4', 'hat 5']

for msg in range(10):
    cat = random.choice(cats)
    hat = random.choice(hats)
    print('publish: %s - %s' % (cat, hat))
    conn.publish(cat, hat)
