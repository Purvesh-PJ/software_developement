from book import Book
from library import Library
from user import User


def main():
    # Create instances of Book
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book2 = Book("1984", "George Orwell", 1949)

    # Create instances of User
    user1 = User("Alice", 1)
    user2 = User("Bob", 2)

    # Create instance of Library
    library = Library("City Library")

    # Add books and users to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_user(user1)
    library.add_user(user2)

    # User checks out a book
    user1.check_out_book(book1)

    find_book = library.find_book_by_title("The Great Gatsby")
    if find_book:
        print(find_book.title)
    else:
        print("Book not found.")

    find_user = library.find_user_by_id(1)
    if find_user:
        print(find_user.name)
    else:
        print("User not found.")

    # User returns a book
    # user1.return_book(book1)

    # Check the status of the book after return
    print(book1.is_checked_out)  # Output: False


if __name__ == "__main__":
    main()
