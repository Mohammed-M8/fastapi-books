

from pydantic import BaseModel
from sqlalchemy import Update


class BookSchema(BaseModel):
    id:int
    name:str
    author:str
    user_id:int

    class Config:
        orm_mode=True

class CreateBookSchema(BaseModel):
    name:str
    author:str

    class Config:
        orm_mode=True

class UpdateBookSchema(BaseModel):
    name:str
    author:str

    class Config:
        orm_mode=True
