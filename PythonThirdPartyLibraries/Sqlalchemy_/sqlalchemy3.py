from pprint import pprint
from sqlalchemy import Column, Integer, String, create_engine, and_, text, distinct, DDL
from sqlalchemy.dialects.mysql import INTEGER,VARCHAR,YEAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased

engine = create_engine('sqlite:///test2.db', echo=False)
# engine = create_engine("mysql+pymysql://root:1234@localhost/falonie",encoding='utf8', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))
    # addresses = Column(String(50))

    def __repr__(self):
        return "<User(name='%s',fullname='%s',password='%s')>" % (self.name, self.fullname, self.password)


# print(User.__table__)
# print(User.__tablename__)
# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

# add_column = DDL("ALTER TABLE users ADD COLUMN addresses VARCHAR(255)")
# drop_column = DDL("ALTER TABLE users DROP COLUMN addresses")
# modify_column=DDL("ALTER TABLE users MODIFY COLUMN addresses VARCHAR(255)")
# engine.execute(add_column)
# engine.execute(drop_column)
# engine.execute(modify_column)

# user1 = User(name='falonie', fullname='falonie wang', password='aaa')
# print(user1.name)
# print(user1.fullname)
# print(user1.id)
# session.add(user1)
# session.commit()
# our_user=session.query(User).filter_by(name='falonie').first()
# print(our_user)
# our_user2=session.query(User).filter_by().first()
# print(our_user2)
# print(user1 is our_user)
# print(id(user1),id(our_user))
# session.add_all([User(name='wendy', fullname='Wendy Williams', password='foobar'),User(name='mary', fullname='Mary Contrary', password='xxg527'),User(name='fred', fullname='Fred Flinstone', password='blah')])
# session.commit()

# user1.password='bbbbbb'
# update_value=session.query(User).filter(User.name=='falonie',User.fullname=='falonie wang').update({'name':'ffff'})
# print(update_value)
# session.query(User).filter(User.name=='Falonie',User.fullname=='falonie wang').update({'fullname':'Falonie Wang'})
# session.commit()
# print(session.dirty)

# print(session.new)
# print(session.query(User).filter().all())
# print(session.query(User).all())
# for instance in session.query(User).order_by(User.id):
# print(instance.name,instance.fullname)
# print(instance)
# for row in session.query(User,User.name).all():
#     print(row.User,row.name)
# print(row)

user_alias = aliased(User, name='user_alias')
# for row in session.query(user_alias, user_alias.name).all():
#     print(row.user_alias)

# for u in session.query(User).order_by(User.id)[:3]:
#     print(u)

# for u in session.query(User).filter_by(name='falonie'):
#     print(u)

# for u in session.query(User).filter(User.name=='falonie').filter(User.fullname=='falonie wang'):
#     print(u)

# for u in session.query(User).filter(User.name.ilike('%nie%')):
#     print(u)

# print(session.query(User).filter(and_(User.name=='falonie',User.fullname.ilike('falonie w%'))).all())

# print(session.query(User).filter(text("id<:value")).params(value=4).order_by(User.id).all())

# pprint(session.query(User).from_statement(text("SELECT * FROM users")).all())

# pprint(session.query(User).from_statement(text("SELECT * FROM users")).all())

# pprint(session.query(User).from_statement(text("SELECT * FROM users WHERE name=:name")).params(name='falonie').all())

# print(session.query(User).filter(User.name.like('%e%')).count())

jack=User(name='jack',fullname='Jack Bean',password='aaaa')
# print(jack.addresses)