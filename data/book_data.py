from models.book import BookModel
from data.user_data import user_list


def create_test_books():
    book1 = BookModel(
        name="Clean Code",
        author="Robert C. Martin",
        user=user_list[0]
    )

    book2 = BookModel(
        name="The Pragmatic Programmer",
        author="Andrew Hunt",
        user=user_list[1]
    )

    book3 = BookModel(
        name="Atomic Habits",
        author="James Clear",
        user=user_list[2]
    )

    book4 = BookModel(
        name="Deep Work",
        author="Cal Newport",
        user=user_list[3]
    )

    book5 = BookModel(
        name="The Alchemist",
        author="Paulo Coelho",
        user=user_list[4]
    )

    return [book1, book2, book3, book4, book5]


book_list = create_test_books()