from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from dependencies.get_current_user import get_current_user
from models.review import ReviewModel
from models.user import UserModel
from serializers.review import CreateReviewSchema, UpdateReviewSchema

router=APIRouter()

@router.get("/reviews")
def get_reviews(db:Session=Depends(get_db)):
    reviews=db.query(ReviewModel).all()
    return reviews;

@router.get("/reviews/{review_id}")
def get_review(review_id:int,db:Session=Depends(get_db)):
    review=db.query(ReviewModel).filter(ReviewModel.id==review_id).first()
    if not review:
        raise HTTPException(404,"Review not found")

    return review

@router.post("/books/{book_id}/reviews",status_code=201)
def create_review(book_id:int,data:CreateReviewSchema,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
    review=ReviewModel(**data.model_dump(),book_id=book_id,user_id=user.id)
    db.add(review)
    db.commit()

    db.refresh(review)
    return review;

@router.put("/reviews/{review_id}")
def update_review(review_id:int,data:UpdateReviewSchema,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
    review=db.query(ReviewModel).filter(ReviewModel.id==review_id).first()
    if not review:
        raise HTTPException(404,"review not found")

    if review.user_id!=user.id:#type:ignore
        raise HTTPException(403,"Forbidden")


    new_review=data.model_dump()
    for key,value in new_review.items():
        setattr(review,key,value)
    db.commit()
    db.refresh(review)
    return review

@router.delete("/reviews/{review_id}",status_code=204)
def delete_review(review_id:int,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
    review=db.query(ReviewModel).filter(ReviewModel.id==review_id).first()
    if not review:
        raise HTTPException(404,"review not found")

    if review.user_id!=user.id:#type:ignore
            raise HTTPException(403,"Forbidden")
    db.delete(review)
    db.commit()
    return None
