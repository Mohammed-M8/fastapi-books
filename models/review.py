from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.base import BaseModel


class ReviewModel(BaseModel):

    __tablename__="reviews"

    id=Column(Integer,primary_key=True,index=True)
    book_id=Column(Integer,ForeignKey("books.id"),nullable=False)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)

    book=relationship("BookModel",back_populates="reviews")
    user=relationship("UserModel",back_populates="reviews")
