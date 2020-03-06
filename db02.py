import sqlalchemy as sa

conn = sa.create_engine('sqlite://')

# control db by using expression language
meta = sa.MetaData()
zoo = sa.Table('zoo', meta,
               sa.Column('critter', sa.String, primary_key=True),
               sa.Column('count', sa.Integer),
               sa.Column('damages', sa.Float))
meta.create_all(conn)

conn.execute(zoo.insert(('duck', 10, 0.0)))
conn.execute(zoo.insert(('dubearck', 2, 1000.0)))
conn.execute(zoo.insert(('tiger', 1, 2000.0)))


rows = conn.execute(zoo.select())

for row in rows:
    print(row)
