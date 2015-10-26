__author__ = 'Kim'
from insa.database.engine import Base, engine
from sqlalchemy import Integer,DateTime, String, Column, func

class Standard(Base):
    __tablename__ = 'standard'
    subject = Column(String(255), unique= True, primary_key= True)
    standard = Column(Integer)
    created = Column(DateTime, default=func.now())
    modified = Column(DateTime)
    course = Column(String(255))

    Base.metadata.create_all(engine)
