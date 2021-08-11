import datetime
from sqlalchemy import *
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship,backref
from base import Base
from log_info import *


class Library(Base):
    __tablename__ = "library"
    book_id       = Column(Integer, primary_key=True,autoincrement=True)
    book_name     = Column(String)
    edition_year  = Column(Integer)
    author        = Column(String)
    owner_name    = Column(String)
    category      = Column(String)
    translator    = Column(String)
    date_time     = Column(String)
    log_id        = relationship('Log_info', lazy=True)

    def __init__(self,book_name:str,edition_year:int,author:str,owner_name:str,category:str,translator:str):
        self.book_name    = book_name
        self.edition_year = edition_year
        self.author       = author
        self.owner_name   = owner_name
        self.category     = category
        self.translator   = translator
        self.date_time    = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")