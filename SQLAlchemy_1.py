from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,ForeignKey
import sqlalchemy

print(sqlalchemy.__version__)
engine=create_engine('sqlite:///foo.db',echo=True)
metadata=MetaData(engine)

