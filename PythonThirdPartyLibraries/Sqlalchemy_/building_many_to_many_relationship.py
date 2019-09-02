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
post_keywords = Table('post_keywords', Base.metadata, Column('post_id', ForeignKey('posts.id'), primary_key=True),
                      Column('keyword_id', ForeignKey('keywords.id'), primary_key=True))


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


class BlogPost(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    headline = Column(String(255), nullable=False)
    keywords = relationship('Keyword', secondary=post_keywords, back_populates='posts')
    # author=relationship(Us)

    def __init__(self, headline, body, author):
        self.author = author
        self.headline = headline
        self.body = body

    def __repr__(self):
        return "BlogPost(%r, %r, %r)" % (self.headline, self.body, self.body)


class Keyword(Base):
    __tablename__ = 'keywords'
    id = Column(Integer, primary_key=True)
    keyword = Column(String(50), nullable=False)
    posts = relationship('BlogPost', secondary=post_keywords, back_populates='keywords')

    def __init__(self, keyword):
        self.keyword = keyword

    def __repr__(self):
        return "Keyword(%r, %r)" % (self.id, self.keyword)


BlogPost.author = relationship(User, back_populates="posts")
User.posts = relationship(BlogPost, back_populates="author", lazy="dynamic")
# Base.metadata.create_all(engine)
# wendy=[User(name='wendy',fullname='wendy wd',password='wwww')]
# session.add_all(wendy)
# session.commit()
wendy=session.query(User).filter_by(name='wendy').one()
post=BlogPost("wendy's blog post.","This is a test.",wendy)
# session.add(post)
# session.commit()
post.keywords.append(Keyword('wendyyy'))
post.keywords.append(Keyword('firstpost'))
print(session.query(BlogPost).filter(BlogPost.keywords).all())
# print(wendy)
# session.add(post)
# session.commit()
