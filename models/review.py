
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.base import BaseModel
from .book import BookModel

class ReviewModel(BaseModel):

    __tablename__="reviews"

    id=Column(Integer,primary_key=True,index=True)
    comment=Column(String)
    rating=Column(Integer,nullable=False)
    book_id=Column(Integer,ForeignKey("books.id"),nullable=False)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)

    book=relationship("BookModel",back_populates="reviews")
    user=relationship("UserModel",back_populates="reviews")
