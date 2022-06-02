from unittest import TestCase, main
from project.room import Room



class TestRoom(TestCase):
    def setUp(self):
        self.room1 = Room("Dobrev", 100, 2)
        self.room1.children = []
        self.room1._expenses = 0

    def test_init(self):
        self.assertEqual("Dobrev", self.room1.family_name)


if __name__ == '__main__':
    main()
