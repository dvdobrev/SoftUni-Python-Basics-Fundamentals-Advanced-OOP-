from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.sharo = Mammal("Sharo", "dogs", "Woof woof")
        self.sharo.__kingdom = "animals"

    def test_check_init_initilization(self):
        self.assertEqual("Sharo", self.sharo.name)
        self.assertEqual("dogs", self.sharo.type)
        self.assertEqual("Woof woof", self.sharo.sound)
        self.assertEqual("animals", self.sharo._Mammal__kingdom)

    def test_make_sound(self):
        result = self.sharo.make_sound()
        self.assertEqual("Sharo makes Woof woof", result)

    def test_get_kingdom(self):
        result = self.sharo.get_kingdom()
        self.assertEqual("animals", result)

    def test_get_info(self):
        result = self.sharo.info()
        self.assertEqual("Sharo is of type dogs", result)


if __name__ == '__main__':
    main()
