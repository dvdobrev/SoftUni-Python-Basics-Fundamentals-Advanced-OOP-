from unittest import TestCase, main

from project.player.advanced import Advanced


class TestAdvanced(TestCase):
    def setUp(self):
        self.player = Advanced("Test")

    def test_init(self):
        self.assertEqual(self.player.username, "Test")
        self.assertEqual(self.player.default_health_points, 250)

    def test_username_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.player.username = ""
        self.assertEqual(str(ex.exception), "Player's username cannot be an empty string.")

    def test_health_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.player.health = -5
        self.assertEqual(str(ex.exception), "Player's health bonus cannot be less than zero.")

    def test_take_damage_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.player.take_damage(-5)
        self.assertEqual(str(ex.exception), "Damage points cannot be less than zero.")

    def test_player_is_not_dead(self):
        self.assertFalse(self.player.is_dead)


if __name__ == '__main__':
    main()
