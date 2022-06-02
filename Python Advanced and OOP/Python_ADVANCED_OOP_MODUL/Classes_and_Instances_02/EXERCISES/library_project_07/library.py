class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        self.user_records.append(user)

    def remove_user(self, user):
        if user in self.user_records:
            self.user_records.remove(user)

        else:
            return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str):
        for id in self.user_records:
            if user_id == id.user_id and new_username == id.username:
                return f"Please check again the provided username - it should be different than the username used so far!"

            elif user_id == id.user_id and not new_username == id.username:
                old_username = id.username
                id.username = new_username
                if old_username in self.rented_books:
                    self.rented_books[new_username] = self.rented_books.pop(old_username)

                return f"Username successfully changed to: {new_username} for userid: {user_id}"

        return f"There is no user with id = {user_id}!"  # It is possible to have a mistake here
