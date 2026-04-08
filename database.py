from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()


Database_URL=os.getenv('Database_URL')

engine=create_async_engine(Database_URL,echo=True)

async_session=async_sessionmaker(
    engine, expire_on_commit=False,class_=AsyncSession
)

class Base(DeclarativeBase):
    pass
