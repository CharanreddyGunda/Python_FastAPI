from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    gender= Column(String)
    age= Column(Integer)