class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            library.books_available[author].remove(book_name)
            # library.rented_books[self.username][book_name] = days_to_return
            if self.username in library.rented_books:
                library.rented_books[self.username].update({book_name: days_to_return})

            else:
                library.rented_books[self.username] = {book_name: days_to_return}
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for user in library.rented_books:
            if book_name in library.rented_books[user]:
                return f'The book "{book_name}" is already rented and will be available in {library.rented_books[user][book_name]} days!'

    def return_book(self, author: str, book_name: str, library):
        for user in library.rented_books:
            if book_name in library.rented_books[user]:
                library.books_available[author].append(book_name)
                del library.rented_books[user][book_name]
                self.books.remove(book_name)
            else:
                return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        result = ", ".join(sorted(self.books))
        return result

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
