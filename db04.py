import dbm

filename = 'a.dbm'

db = dbm.open(filename, 'c')  # r:read-only, w:write, c:able to read and write
db['duck'] = 'aa'
db['dubearck'] = 'bb'
db['tiger'] = 'cc'
db.close()

db = dbm.open(filename, 'r')

print(db['duck'])
print(db['dubearck'])
print(db['tiger'])

db.close()
