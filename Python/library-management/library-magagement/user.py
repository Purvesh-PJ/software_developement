from book import Book


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.checked_out_books = []

    def check_out_book(self, book: Book):
        if book.check_out():
            self.checked_out_books.append(book)
            print(f"{self.name} checked out {book.title}.")
        else:
            print(f"{book.title} is already checked out.")

    def return_book(self, book: Book):
        if book in self.checked_out_books and book.return_book():
            self.checked_out_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} cannot return {book.title}.")
