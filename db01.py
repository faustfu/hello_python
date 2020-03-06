# 1. Module:sqlalchemy is for db processing.
import sqlalchemy as sa

conn = sa.create_engine('sqlite://')

# control db by using SQL directly
insert_sql = 'insert into zoo(critter, count, damages) values(?, ?, ?)'
select_sql = 'select * from zoo'

conn.execute('''
create table zoo(
  critter varchar(20) primary key,
  count int,
  damages float
)
''')


conn.execute(insert_sql, 'duck', 10, 0.0)
conn.execute(insert_sql, 'bear', 2, 1000.0)
conn.execute(insert_sql, 'tiger', 1, 2000.0)

rows = conn.execute(select_sql)

for row in rows:
    print(row)
