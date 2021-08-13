from app import Base
import datetime
from sqlalchemy import Column,Integer,String,ForeignKey
from base import Base
from sqlalchemy.orm import relationship


class Log_info(Base):
    __tablename__ = "log_info"
    book_id_log   = Column(Integer,primary_key=True)
    date_time     = Column(String)
    process       = Column(String)
    lib_id        = Column(Integer,ForeignKey("library.book_id"))
    lib           = relationship("Library", back_populates="log_id")

    def __init__(self,process:str):
        self.process    = process
        self.date_time  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")