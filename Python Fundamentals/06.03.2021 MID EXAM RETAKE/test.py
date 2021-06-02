# books = ["a", "b", "c", "d", "f"]
# print(books)
# book1 = books.index("c")
# book2 = books.index("f")
# books[book1], books[book2] = books[book2], books[book1]
# print(books)

digits = [1, 2, 3, 4, 5, 6, 7, 8] # 4 2 3 7 5 6 1 8
print(digits)
dig1 = digits.index(4)
dig2 = digits.index(1)
dig3 = digits.index(7)
# 4 1 7    7 4 1
digits[dig1], digits[dig2], digits[dig3] = digits[dig3], digits[dig1], digits[dig2]
print(digits)