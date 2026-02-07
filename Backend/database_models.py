from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Float,DateTime
import datetime
Base=declarative_base()

class Product(Base):
    
    __tablename__="products"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    price=Column(Float)
    description=Column(String)
    quantaity=Column(Integer)


    quantaity=Column(Integer)


class ItemHistory(Base):
    __tablename__ = "item_history"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=True)
    name = Column(String)
    action = Column(String) # "ADDED" or "DELETED"
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
