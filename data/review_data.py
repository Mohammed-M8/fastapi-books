from models.review import ReviewModel
from data.user_data import user_list
from data.book_data import book_list


def create_test_reviews():
    review1 = ReviewModel(
        comment="Great book for learning good programming practices.",
        rating=5,
        book=book_list[0],
        user=user_list[1]
    )

    review2 = ReviewModel(
        comment="Very useful for understanding software development principles.",
        rating=5,
        book=book_list[1],
        user=user_list[2]
    )

    review3 = ReviewModel(
        comment="Simple and practical. Easy to apply.",
        rating=4,
        book=book_list[2],
        user=user_list[3]
    )

    review4 = ReviewModel(
        comment="Some really useful ideas about focusing on important work.",
        rating=4,
        book=book_list[3],
        user=user_list[4]
    )

    review5 = ReviewModel(
        comment="A short but memorable story.",
        rating=5,
        book=book_list[4],
        user=user_list[0]
    )

    return [review1, review2, review3, review4, review5]


review_list = create_test_reviews()