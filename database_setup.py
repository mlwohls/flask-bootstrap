import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# packages for automapping
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

##########################


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    password = Column(String(80), nullable = False)

class AuthKeys(Base):
    __tablename__ = 'auth_keys'
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    password = Column(String(80), nullable = False)











################ insert at end of file ####################

engine = create_engine('postgresql://mlwohls2:12temp34@bootstrap-db.chwr0n3sezpi.us-east-1.rds.amazonaws.com/flask_bootstrap')
Base.metadata.create_all(engine)
