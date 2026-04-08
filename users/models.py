from database import Base
from sqlalchemy import (ForeignKey,
            Column,String,Integer,
            DateTime,Text,Numeric
                        )
from datetime import datetime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True,nullable=False)
    first_name=Column(String(30))
    last_name=Column(String(30))
    email=Column(String(50),unique=True)
    password=Column(String,nullable=False)
    created_at = Column(DateTime, default=datetime.now())


