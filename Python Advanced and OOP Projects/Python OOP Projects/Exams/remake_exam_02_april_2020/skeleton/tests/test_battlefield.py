from unittest import TestCase, main

from project.battle_field import BattleField
from project.card.trap_card import TrapCard
from project.player.beginner import Beginner


class TestBattleField(TestCase):

    def setUp(self):
        self.attacker = Beginner("attacker")
        self.enemy = Beginner("enemy")
        self.trap_card = TrapCard("trap")

    def test_player_is_not_dead(self):
        result1 = self.attacker.is_dead
        self.assertFalse(result1)
        result2 = self.enemy.is_dead
        self.assertFalse(result2)

    def test_player_is_dead(self):
        self.attacker.health = 0
        with self.assertRaises(ValueError) as ex:
            BattleField().fight(self.attacker, self.enemy)
        self.assertEqual(str(ex.exception), "Player is dead!")


    def test_if_player_is_beginner_get_bonus_health_and_damage_points(self):
        self.attacker.card_repository.cards.append(self.trap_card)
        # b = BattleField()
        # b.fight(self.attacker, self.enemy)
        self.assertEqual(self.attacker.health, 90)
        self.assertEqual(self.attacker.card_repository.get_card_total_damage(), 150)




if __name__ == '__main__':
    main()