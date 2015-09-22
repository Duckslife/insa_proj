# -*- coding: utf-8 -*-

from __future__ import absolute_import

from sqlalchemy import Column
from sqlalchemy import Integer, Float, DateTime, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base, declared_attr


class BaseModel(object):
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=func.now())
    modfied = Column(DateTime)

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()

    @classmethod
    def fields(cls):
        l = []
        for k in cls.FIELDS.keys():
            l.append(cls.__dict__[k])
        print (l)
        return l

    def to_dict(self):
        intersection = set(self.__table__.columns.keys()) & set(self.FIELDS)
        return dict(map(
            lambda key:
                (key, (lambda value: self.FIELDS[key](value) if value is not None else None)(getattr(self, key))),
            intersection))

    FIELDS = {
            'id': str,
            'created': str,
            'modified': str,
    }

Base = declarative_base(cls=BaseModel)

