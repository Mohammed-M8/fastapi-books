from typing import List

from fastapi import APIRouter, Depends, HTTPException

from data import book_data
from database import get_db
from dependencies.get_current_user import get_current_user
from models.book import BookModel
from models.user import UserModel
from serializers.book import BookSchema, CreateBookSchema, UpdateBookSchema
from sqlalchemy.orm import Session

router=APIRouter()

@router.get("/books",response_model=List[BookSchema])
def get_all_books(db:Session=Depends(get_db)):
    books=db.query(BookModel).all()
    return books

@router.get("/books/{book_id}",response_model=BookSchema)
def get_single_book(book_id:int,db:Session=Depends(get_db)):
    book=db.query(BookModel).filter(BookModel.id==book_id).first()
    if not book:
        raise HTTPException(404,"Book not found")
    return book

@router.post("/books",response_model=BookSchema,status_code=201)
def create_book(new_book:CreateBookSchema,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
    book=BookModel(**new_book.model_dump(),user_id=user.id)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

@router.put("/books/{book_id}",response_model=BookSchema,status_code=204)
def update_book(book_id:int,update:UpdateBookSchema,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
    book=db.query(BookModel).filter(BookModel.id==book_id).first()
    if not book:
        raise HTTPException(404,"Book not found")
    book_data=update.model_dump(exclude_unset=True)

    for key,value in book_data.items():
        setattr(book,key,value)

    db.commit()
    db.refresh(book)
    return book

@router.delete("/teas/{book_id}")
def delete_book(book_id:int,db:Session=Depends(get_db)):
    book=db.query(BookModel).filter(BookModel.id==book_id).first()

    db.delete(book)
    db.commit()
    return None


