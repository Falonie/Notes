from pprint import pprint
from sqlalchemy import Column, Integer, String, create_engine, and_, text, ForeignKey, DDL, Table, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, relationship

engine = create_engine('sqlite:///test.db', echo=False)
# engine = create_engine("mysql+pymysql://root:1234@localhost/falonie",encoding='utf8', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()
association_table = Table('association', Base.metadata, Column('left_id', Integer, ForeignKey('left.id')),
                          Column('right_id', Integer, ForeignKey('right.id')))


class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    # children = relationship("Child", secondary=association_table, back_populates="parents")
    children = relationship("Child", secondary=association_table, backref="parents")

    def __repr__(self):
        return "<Parent(id={!s}, name={!s})>".format(self.id, self.name)


class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    # parents = relationship("Parent", secondary=association_table, back_populates="children")

    def __repr__(self):
        return "<Child(id={!s}, name={!s})>".format(self.id, self.name)


Base.metadata.create_all(engine)
# if __name__ == '__main__':