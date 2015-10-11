from sqlalchemy import String, Column, Integer, DateTime, func
from insa.database.engine import Base, engine


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=func.now())
    modified = Column(DateTime)
    name = Column(String, nullable=False)
    role = Column(String)
    division = Column(String)

Base.metadata.create_all(engine)

