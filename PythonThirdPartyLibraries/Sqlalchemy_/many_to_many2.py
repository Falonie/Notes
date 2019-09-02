from pprint import pprint
from sqlalchemy import Column, Integer, String, create_engine, and_, text, ForeignKey, DDL, Table, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, relationship

engine = create_engine('sqlite:///test.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

registrations = Table('registrations', Base.metadata, Column('student_id', Integer, ForeignKey('students.id')),
                      Column('class_id', Integer, ForeignKey('classes.id')))


# registrations = Table('registrations', Base.metadata, Column('student_id', Integer, ForeignKey('students.id')),
#                           Column('class_id', Integer, ForeignKey('classes.id')))


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    classes = relationship("Class", secondary=registrations, backref="students")

    def __repr__(self):
        return "<Student(id={!s}, name={!s})>".format(self.id, self.name)


class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return "<Class(id={!s}, name={!s})>".format(self.id, self.name)


# class Student(Base):
#     __tablename__ = 'students'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     classes = relationship("Class", secondary=registrations, backref="students")
#
#     def __repr__(self):
#         return "<Student(id={!s}, name={!s})>".format(self.id, self.name)
#
#
# class Class(Base):
#     __tablename__ = 'classes'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     # parents = relationship("Parent", secondary=association_table, back_populates="children")
#
#     def __repr__(self):
#         return "<Class(id={!s}, name={!s})>".format(self.id, self.name)

# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

class InsertValues(object):
    @staticmethod
    def value():
        susan = Student(name='Susan')
        susan.classes = [Class(name='Python'), Class(name='JavaScript'), Class(name='Java')]
        session.add_all([susan])
        session.commit()

    @staticmethod
    def value2():
        jack = Student(name='Jack')
        smith = Student(name='Smith')
        jack.classes = [Class(name='Python'), Class(name='C'), Class(name='iOS')]
        smith.classes = [Class(name='Python'), Class(name='C++'), Class(name='iOS')]
        session.add_all([jack, smith])
        session.commit()


# InsertValues.value2()
