import sqlalchemy
from sqlalchemy import Column,Integer,String, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base as Base
Base = Base()

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
    log_id        = relationship("LogInfo", back_populates="library")

    def __init__(self,book_name:str,edition_year:int,author:str,owner_name:str,category:str,translator:str):
        self.book_name    = book_name
        self.edition_year = edition_year
        self.author       = author
        self.owner_name   = owner_name
        self.category     = category
        self.translator   = translator
        self.date_time    = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class LogInfo(Base):
    __tablename__ = "loginfo"
    book_id_log   = Column(Integer,primary_key=True)
    date_time     = Column(String)
    process       = Column(String)
    lib_id        = Column(Integer,ForeignKey("library.book_id"))
    library       = relationship("Library", back_populates="log_id")

    def __init__(self,process:str,lib_id:int):
        self.process    = process
        self.date_time  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.lib_id     = lib_id

engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)

