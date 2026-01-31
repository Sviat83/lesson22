from sqlalchemy import Column, Integer, String
from database import Base

class UserModel(Base):
    __tablename__ = "users2"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)
    last_name = Column(String)
