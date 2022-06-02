from unittest import TestCase, main
from project.card.magic_card import MagicCard


class TestMagicCard(TestCase):
    def setUp(self):
        self.card = MagicCard("Test_card")

    def test_init(self):
        self.assertEqual(self.card.name, "Test_card")
        self.assertEqual(self.card.default_card_damage_points, 5)
        self.assertEqual(self.card.default_card_health_points, 80)

    def test_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.card.name = ""
        self.assertEqual(str(ex.exception), "Card's name cannot be an empty string.")

    def test_magic_point_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.card.damage_points = -5
        self.assertEqual(str(ex.exception), "Card's damage points cannot be less than zero.")

    def test_health_points_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.card.health_points = -5
        self.assertEqual(str(ex.exception), "Card's HP cannot be less than zero.")


if __name__ == '__main__':
    main()
