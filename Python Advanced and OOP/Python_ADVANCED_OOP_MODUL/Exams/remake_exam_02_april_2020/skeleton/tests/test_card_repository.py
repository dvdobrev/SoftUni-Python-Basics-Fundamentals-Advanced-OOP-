from unittest import TestCase, main

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(TestCase):
    def setUp(self):
        self.test_repository = CardRepository()
        self.test_card = MagicCard("Test")

    def test_init(self):
        self.assertEqual(self.test_repository.count, 0)
        self.assertEqual(self.test_repository.cards, [])

    def test_add__card_exist_raises(self):
        with self.assertRaises(ValueError)as ex:
            self.test_repository.add(self.test_card)
            self.test_repository.add(self.test_card)
        # self.assertEqual(str(ex.exception), f"Card {self.test_card.name} already exists!")

    def test_add__card(self):
        self.test_repository.add(self.test_card)
        self.assertEqual(len(self.test_repository.cards), 1)
        self.assertEqual(self.test_repository.count, 1)

    def test_remove__raises(self):
        with self.assertRaises(ValueError) as ex:
            self.test_repository.remove("")
        self.assertEqual(str(ex.exception), f"Card cannot be an empty string!")

    def test_remove(self):
        self.test_repository.add(self.test_card)
        self.test_repository.remove("Test")
        self.assertEqual(len(self.test_repository.cards), 0)
        self.assertEqual(self.test_repository.count, 0)

    def test_find(self):
        self.test_repository.add(self.test_card)
        result = self.test_repository.find("Test")
        self.assertEqual(self.test_card, result)


if __name__ == '__main__':
    main()
