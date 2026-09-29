import email

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.base import BaseModel


class BookModel(BaseModel):
    __tablename__="books"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,unique=True)
    author=Column(String)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    user=relationship("UserModel",back_populates="books")

    