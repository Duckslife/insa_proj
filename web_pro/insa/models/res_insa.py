# -*- coding: utf-8 -*-

from sqlalchemy import Integer,DateTime, String, Column, ForeignKey, func
from insa.database.engine import Base, engine
from sqlalchemy.orm import relationship, backref

class Res(Base):
    __tablename__ = 'res_insa'
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=func.now())
    modified = Column(DateTime)
    course = Column(String(255))
    subject = Column(String(255))
    mark = Column(Integer)
    emp_id = Column(Integer, ForeignKey('employee.id'))

    employee = relationship("Employee", backref = backref("res_insa"))

    Base.metadata.create_all(engine)