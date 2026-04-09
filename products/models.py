from database import Base
from sqlalchemy import (ForeignKey,
            Column,String,Integer,
            DateTime,Text,Numeric
                        )
from datetime import datetime
from sqlalchemy.orm import relationship
# class Category(Base):
#     __tablename__ = 'categories'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(20))
#     created_at = Column(DateTime, default=datetime.now())
#     user_id=Column(Integer,ForeignKey("users.id"))
#
#     products = relationship('Products', back_populates='category')


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    desc = Column(Text, nullable=False)
    price = Column(Numeric(10, 2))
    # category_id = Column(Integer, ForeignKey('categories.id'))
    created_at = Column(DateTime, default=datetime.now())

    # category = relationship('Category', back_populates='products')
    # order = relationship('Orders', back_populates='products')
    # user_id=Column(Integer,ForeignKey("users.id"))
