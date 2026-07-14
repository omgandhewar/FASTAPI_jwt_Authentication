from db.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__="user"
    
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False)
    password=Column(String,nullable=False)
    
    
class token(Base):
    __tablename__="token_id"
    
    id=Column(Integer,primary_key=True)
    jti=Column(String,nullable=False)
    refresh_token=Column(String)