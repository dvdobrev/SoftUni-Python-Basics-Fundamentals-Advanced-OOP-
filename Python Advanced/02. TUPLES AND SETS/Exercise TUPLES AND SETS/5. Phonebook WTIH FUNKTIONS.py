def fill_phone_book():
    data = input()
    phone_book = {}
    while not data.isnumeric():
        name, number = data.split("-")
        phone_book[name] = number
        data = input()
    return phone_book, int(data)


def searched_contact(contact_name, phone_book):

    if contact_name in phone_book:
        print(f"{contact_name} -> {phone_book[contact_name]}")

    else:
        print(f"Contact {contact_name} does not exist.")

phone_book, iterations_count = fill_phone_book()

for _ in range(iterations_count):
    name = input()
    searched_contact(name, phone_book)