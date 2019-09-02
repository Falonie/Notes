from pprint import pprint
from sqlalchemy import Column, Integer, String, create_engine, and_, text, ForeignKey, DDL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, relationship

# from PythonThirdPartyLibraries.Sqlalchemy_.sqlalchemy3 import User

engine = create_engine('sqlite:///test1.db', echo=False)
# engine = create_engine("mysql+pymysql://root:1234@localhost/falonie",encoding='utf8', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()


# with engine.connect() as connection:
#     sql = 'SELECT * FROM python_areas_province_city_county_name'
#     result = connection.execute(sql)
#     for item in result:
#         print(item)
# pprint(session.query(User).from_statement(text("SELECT * FROM users WHERE name=:name")).params(name='falonie').all())

# print(session.query(User).filter(User.name.like('%e%')).count())

# class Address(Base):
#     __tablename__ = 'addresses'
#     id = Column(Integer, primary_key=True)
#     email_address = Column(String(50), nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     user = relationship("User", back_populates="addresses")
#
#     def __repr__(self):
#         return "<Address(email_address='%s')>" % self.email_address

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))
    # addresses=relationship("Address",back_populates="user")
    addresses = relationship("Address", backref="users")

    def __repr__(self):
        return "<User(name='%s',fullname='%s',password='%s')>" % (self.name, self.fullname, self.password)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    # user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


# User.addresses=relationship("Address",order_by=Address.id,back_populates="user")
# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
# add_column = DDL("ALTER TABLE users ADD COLUMN addresses")
# engine.execute(add_column)

# session.add_all([User(name='wendy', fullname='Wendy Williams', password='foobar'),User(name='mary', fullname='Mary Contrary', password='xxg527'),User(name='fred', fullname='Fred Flinstone', password='blah')])
# session.commit()

# jack = User(name='jack', fullname='Jack Bean', password='aaaa')
# print(jack.addresses)
# jack.addresses=[Address(email_address='jack@gmail.com'),Address(email_address='jack@outlook.com'),]
# session.add_all([jack])
# session.commit()
# print(jack.addresses[1].user)
# jack=session.query(User).filter_by(name='jack').one()
# print(jack.addresses)

# pprint(session.query(User,Address).filter(User.id==Address.id).all())
# pprint(session.query(User).join(Address).filter().all())