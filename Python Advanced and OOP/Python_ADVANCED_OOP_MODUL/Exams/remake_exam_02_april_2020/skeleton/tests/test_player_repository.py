from unittest import TestCase, main

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(TestCase):
    def setUp(self):
        self.test_repository = PlayerRepository()
        self.test_player = Beginner("Test")

    def test_init(self):
        self.assertEqual(self.test_repository.count, 0)
        self.assertEqual(self.test_repository.players, [])

    def test_add__player_exist_raises(self):
        with self.assertRaises(ValueError)as ex:
            self.test_repository.add(self.test_player)
            self.test_repository.add(self.test_player)
        self.assertEqual(str(ex.exception), f"Player {self.test_player.username} already exists!")

    def test_add__player(self):
        self.test_repository.add(self.test_player)
        self.assertEqual(len(self.test_repository.players), 1)
        self.assertEqual(self.test_repository.count, 1)

    def test_remove__raises(self):
        with self.assertRaises(ValueError) as ex:
            self.test_repository.remove("")
        self.assertEqual(str(ex.exception), f"Player cannot be an empty string!")

    def test_remove(self):
        self.test_repository.add(self.test_player)
        self.test_repository.remove("Test")
        self.assertEqual(len(self.test_repository.players), 0)
        self.assertEqual(self.test_repository.count, 0)

    def test_find(self):
        self.test_repository.add(self.test_player)
        result = self.test_repository.find("Test")
        self.assertEqual(self.test_player, result)


if __name__ == '__main__':
    main()
