books = input().split("&")
data = input()

while not data == "Done":
    new_data = data.split(" | ")
    command = new_data[0]
    book_name = new_data[1]

    #book_2 = new_data[2]
    if command == "Add Book":
        if book_name not in books:
            books.insert(0, book_name)

    elif command == "Take Book":
        if book_name in books:
            books.remove(book_name)

    elif command == "Swap Books":
        book_2 = new_data[2]
        if book_name in books and book_2 in books:
            book1 = books.index(book_name)
            book2 = books.index(book_2)
            books[book1], books[book2] = books[book2], books[book1]

    elif command == "Insert Book":
        books.append(book_name)

    elif command == "Check Book":
        index = int(new_data[1])
        if index <= len(books):
            print(books[index])

    data = input()

print(", ".join(books))
