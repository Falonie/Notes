from pprint import pprint
from sqlalchemy import Column, Integer, String, create_engine, and_, text, ForeignKey, DDL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, relationship, backref

# engine = create_engine('sqlite:///test2.db', echo=False)
engine = create_engine("mysql+pymysql://root:1234@localhost/falonie", encoding='utf8', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    age = Column(Integer, default=0)
    role_id = Column(Integer, ForeignKey('Roles.id'))
    # role = relationship('Role', foreign_keys='User.role_id')
    role = relationship('Role', foreign_keys='User.role_id', backref=backref('users'))

    def __repr__(self):
        return "<User(id={!s}, name={!s}, age={}, role_id={})>".format(self.id, self.name, self.age, self.role_id)


class Role(Base):
    __tablename__ = 'Roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    # users = relationship('User', foreign_keys='User.role_id')
    def __repr__(self):
        return "<Role(id={!s}, name={!s})>".format(self.id, self.name)


# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)
def create_users_roles():
    # try:
    new_roles = [Role(id=1, name='student'), Role(id=2, name='teacher')]
    session.add_all(new_roles)
    session.commit()
    new_users = [User(name='Curry', age=30, role_id=1), User(name='Durant', age=30, role_id=2),
                 User(name='James', age=33, role_id=1)]
    session.add_all(new_users)
    # new_users2 = [User(name='Curry', age=31, role_id=1)]
    # session.add_all(new_users2)
    session.commit()
    # except Exception as e:
    #     session.rollback()

# create_users_roles()

# pprint(session.query(User).filter(User.role_id).all())
# pprint(session.query(User).filter_by(role_id=1).all())

# pprint(session.query(User).filter(User.role_id==Role.id).all())
# if __name__ == '__main__':
