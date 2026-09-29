from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.environment import DATABASE_URL
from models.base import BaseModel

# Import all models so SQLAlchemy registers them
from models.user import UserModel
from models.book import BookModel
from models.review import ReviewModel

from data.user_data import user_list
from data.book_data import book_list
from data.review_data import review_list


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


try:
    print("Recreating database...")

    BaseModel.metadata.drop_all(bind=engine)
    BaseModel.metadata.create_all(bind=engine)

    print("Seeding the database...")

    db = SessionLocal()

    db.add_all(user_list)
    db.add_all(book_list)
    db.add_all(review_list)

    db.commit()
    db.close()

    print("Database seeding complete! 👋")

except Exception as e:
    print("An error occurred:", e)