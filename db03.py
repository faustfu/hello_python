import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

conn = sa.create_engine('sqlite:///zoo.db')

# control db by using ORM
Base = declarative_base()


class Zoo(Base):
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)

    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages

    def __repr__(self):
        return "<Zoo({},{},{})>".format(self.critter, self.count, self.damages)


Base.metadata.create_all(conn)

a = Zoo('duck', 10, 0.0)
b = Zoo('dubearck', 2, 1000.0)
c = Zoo('tiger', 1, 2000.0)

Session = sessionmaker(bind=conn)
session = Session()

session.add(a)
session.add_all([b, c])

session.commit()
