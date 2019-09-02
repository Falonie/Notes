from sqlalchemy import Column, Integer, String, create_engine, and_, text, distinct, DDL, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, YEAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, relationship

# engine = create_engine('sqlite:///test2.db', echo=False)
engine = create_engine("mysql+pymysql://root:1234@localhost/falonie", encoding='utf8', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    user_id = Column(Integer, ForeignKey('user2.id'))
    # users = relationship("User", back_populates="book")
    users = relationship("User", backref="book")

    def __repr__(self):
        return "<Book(id={!s}, name={!s}), user_id={!s})>".format(self.id, self.name, self.user_id)


class User(Base):
    __tablename__ = 'user2'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)

    # books = relationship("Book", back_populates="users2")
    # books = relationship("Book", backref="users2")

    def __repr__(self):
        return "<User(id={}, name={!s})>".format(self.id, self.name)


# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)
# drop_table = DDL("DROP TABLE book")
# engine.execute(drop_table)

def create_user_book():
    # new_users = [User(id=1,name='Bob'),User(id=2,name='James'),User(id=3,name='Westbrook')]
    new_users = [User(name='Bob'), User(name='James'), User(name='Westbrook')]
    session.add_all(new_users)
    session.commit()
    new_books = [Book(name='Python Crash Course', user_id=1), Book(name='Python Cookbook', user_id=1),
                 Book(name='Fluent Python', user_id=2), ]
    session.add_all(new_books)
    session.commit()

# create_user_book()

# truncate_table = DDL("TRUNCATE TABLE user2")
# engine.execute(truncate_table)
# print(new_user.name)
# print(session.query(User).filter(User.id == '5').all())
# print(session.query(User).filter_by(id='5').all())
