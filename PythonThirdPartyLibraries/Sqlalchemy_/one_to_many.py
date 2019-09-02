from pprint import pprint
from sqlalchemy import Column, Integer, String, create_engine, and_, text, distinct, DDL, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, YEAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, relationship

engine = create_engine('sqlite:///test2.db', echo=False)
# engine = create_engine("mysql+pymysql://root:1234@localhost/falonie",encoding='utf8', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    # children = relationship("Child", back_populates="parent")
    children = relationship("Child", backref="parent")

    def __repr__(self):
        return "<Parent(id={!s}, name={!s})>".format(self.id, self.name)


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    parent_id = Column(Integer, ForeignKey('parent.id'))
    # parent = relationship("Parent", back_populates="children")

    def __repr__(self):
        return "<Child(id={!s}, name={!s})>".format(self.id, self.name)


# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

def create_parent_children():
    susan = Parent(name='Susan')
    # session.add(susan)
    # session.commit()
    #
    # print(susan.children)
    susan.children = [Child(name='Tom'), Child(name='Jerry'), Child(name='Kity')]
    # print(susan.children[1])
    session.add_all([susan])
    session.commit()

# create_parent_children()

# pprint(session.query(Parent,Child).filter().all())
# pprint(session.query(Parent,Child).filter(Parent.id==Child.id).all())
# pprint(session.query(Parent).join(Child,Child.id==Parent.id).filter().all())
