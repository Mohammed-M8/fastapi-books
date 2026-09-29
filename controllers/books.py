from typing import List

from fastapi import APIRouter, Depends

from database import get_db
from models.book import BookModel
from serializers.book import BookSchema
from sqlalchemy.orm import Session

router=APIRouter()

@router.get("/books",response_model=List[BookSchema])
def get_all_books(db:Session=Depends(get_db)):
    books=db.query(BookModel).all()
    return books