from sqlalchemy import String, Column
from web_pro.insa.models import Base


class Employee(Base):
    name = Column(String(255), nullable=False)
    role = Column(String(255))
    division = Column(String(255))