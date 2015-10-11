# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from insa.utils.yaml_decoder import post_conn

engine = create_engine(
    "postgresql+psycopg2://%s:%s@%s/%s" % post_conn,
    echo = True,
    isolation_level ="AUTOCOMMIT"
)
print(engine)

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()