import datetime
from sqlalchemy import *
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from library import *
from base import Base

class Log_info(Base):
    __tablename__ = "log_info"
    book_id_log   = Column(Integer,primary_key=True,autoincrement=True)
    date_time     = Column(String)
    process       = Column(String)
    lib_id        = Column(Integer,ForeignKey("library.book_id"),autoincrement=True)

    def __init__(self,process:str,lib_id:int):
        self.process    = process
        self.date_time  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.lib_id     = lib_id