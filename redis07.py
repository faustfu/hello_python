# Use redis to build pubsub mode.
# client
import redis

conn = redis.Redis()

topics = ['cat 3', 'cat 5']

sub = conn.pubsub()

sub.subscribe(topics)

for msg in sub.listen():
    if msg['type'] == 'message':
        cat = msg['channel']
        hat = msg['data']
        print(cat, hat)
