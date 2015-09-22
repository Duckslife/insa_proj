# -*- coding: utf-8 -*-

from sqlalchemy import Integer, String, Column, ForeignKey
from web_pro.insa.models import Base
from sqlalchemy.orm import relationship, backref

class Res_Insa(Base):
    course = Column(String(255))
    subject = Column(String(255))
    mark = Column(Integer)
    emp_id = Column(Integer, ForeignKey('employee.id'))

    employee = relationship("Employee", backref = backref("res_insa"))
