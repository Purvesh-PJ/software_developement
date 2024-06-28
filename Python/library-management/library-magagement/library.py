
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added {book.title} to the library.")

    def add_user(self, user):
        self.users.append(user)
        print(f"User added user {user.name} to the library.")

    def find_book_by_title(self, title: str):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_user_by_id(self, user_id: int):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None





