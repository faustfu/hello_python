# 1. Module:redis is for accessing redis.
import redis

conn = redis.Redis()

# print(conn.keys('*'))
conn.set('test01', 'abc一二三')
print(conn.get('test01'))
conn.setnx('test01', 'abc')  # ignore if exists
print(conn.get('test01'))
print(conn.getset('test01', 'abc'))  # get old value and set new value
print(conn.get('test01'))

conn.mset({'test02': 54.6, 'test03': 200})
print(conn.mget(['test01', 'test02', 'test03']))

conn.delete('test01')
print(conn.mget(['test01', 'test02', 'test03']))

conn.incr('test03')
conn.incr('test03',10)
print(conn.mget(['test01', 'test02', 'test03']))
conn.decr('test03')
conn.decr('test03',10)
print(conn.mget(['test01', 'test02', 'test03']))

conn.incrbyfloat('test02')
conn.incrbyfloat('test02',10)
print(conn.mget(['test01', 'test02', 'test03']))
conn.incrbyfloat('test02', -1)
print(conn.mget(['test01', 'test02', 'test03']))
