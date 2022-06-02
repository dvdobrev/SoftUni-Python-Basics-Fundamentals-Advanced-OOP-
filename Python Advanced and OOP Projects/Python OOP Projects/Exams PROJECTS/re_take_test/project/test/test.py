from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library("test")
        self.library.books_by_authors = {}
        self.library.readers = {}
        self.author = "John"
        self.title = "no title"
        self.reader = "dobri"

    def test_init(self):
        self.assertEqual(self.library.name, "test")
        self.assertEqual(self.library.books_by_authors, {})
        self.assertEqual(self.library.readers, {})


    def test_name_property(self):
        self.library.name = "no name"
        self.assertEqual(self.library.name, "no name")

    def test_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.library.name = ""
        self.assertEqual(str(ex.exception), "Name cannot be empty string!")

    def test_add_book__add_author(self):
        self.library.add_book(self.author, self.title)
        self.assertEqual(self.library.books_by_authors, {"John": ["no title"]})

    def test_add_reader_name_not_in_readers(self):
        self.library.add_reader("dobri")
        self.assertEqual(self.library.readers, {"dobri": []})

    def test_add_reader_raises(self):
        self.library.add_reader("dobri")

        result = self.library.add_reader("dobri")

        self.assertEqual(result, "dobri is already registered in the test library.")

    def test_rent_book_reader_not_in_readers(self):
        result = self.library.rent_book("reader_dobri", "magi_author", "no tittle")
        self.assertEqual(result, "reader_dobri is not registered in the test Library.")


    def test_rent_book_author_not_in_authors(self):
        self.library.add_reader("dobri")
        self.library.add_book("book_author", "book_title")
        result1 = self.library.rent_book("dobri", "magi_author", "no tittle")
        self.assertEqual(result1, "test Library does not have any magi_author's books.")

    def test_rent_book_tittle_not_in_tittles(self):
        self.library.add_reader("dobri")
        self.library.add_book("magi_author", "book_title")

        result2 = self.library.rent_book("dobri", "magi_author", "no tittle")

        self.assertEqual(result2, """test Library does not have magi_author's "no tittle".""")


    def test_append_book_to_reader(self):
        self.library.add_reader("dobri")
        self.library.add_book("magi_author", "book_title")

        self.library.readers[self.library.readers["dobri"]].append(self.library.books_by_authors)

        self.assertEqual(self.library.readers, {'dobri': [{'magi_author': ['book_title']}]})


    def test_del_book(self):
        pass


if __name__ == '__main__':
    main()
