import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# packages for automapping
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

##########################

AutoBase = automap_base()


##### Setup Huntclub Database classes #######

db2 = create_engine('postgresql://udemeb02aj6tg6:p17p03n8l7pr0t8lvsfk1crol6d@ec2-52-201-127-122.compute-1.amazonaws.com/dalsteca66kgv9')
AutoBase.prepare(db2, reflect=True)

# DB2Session = sessionmaker(db2)
# session_hc = DB2Session()

class Candidate(AutoBase):
    __tablename__ = 'candidates'
