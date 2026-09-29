from pydantic import BaseModel


class ReviewSchema(BaseModel):
    id:int
    comment:str|None
    rating:int
    book_id:int
    user_id:int

    class Config:
        orm_mode=True

class CreateReviewSchema(BaseModel):
    comment:str|None
    rating:int

    class Config:
        orm_mode=True

class UpdateReviewSchema(BaseModel):
    comment:str|None
    rating:int