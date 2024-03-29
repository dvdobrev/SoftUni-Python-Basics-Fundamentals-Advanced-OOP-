import unittest
from unittest import TestCase

from project.battle_field import BattleField
from project.card.trap_card import TrapCard
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestController(unittest.TestCase):
    def test_init_controller(self):
        c = Controller()
        self.assertEqual(len(c.player_repository.players), 0)
        self.assertEqual(len(c.card_repository.cards), 0)

    def test_add_players_success(self):
        c = Controller()
        res1 = c.add_player("Beginner", "testBeginner")
        res2 = c.add_player("Advanced", "testAdvanced")
        self.assertEqual(res1, f"Successfully added player of type Beginner with username: testBeginner")
        self.assertEqual(res2, f"Successfully added player of type Advanced with username: testAdvanced")

    def test_add_cards_success(self):
        c = Controller()
        res1 = c.add_card("Magic", "test1")
        res2 = c.add_card("Trap", "test2")
        self.assertEqual(res1, f"Successfully added card of type MagicCard with name: test1")
        self.assertEqual(res2, f"Successfully added card of type TrapCard with name: test2")

    def test_add_player_card(self):
        c = Controller()
        c.add_player("Beginner", "testBeginner")
        c.add_card("Magic", "test1")
        res = c.add_player_card("testBeginner", "test1")
        self.assertEqual(res, f"Successfully added card: test1 to user: testBeginner"
                         )

    def test_fight(self):
        attacker = Advanced("Test1")
        enemy = Beginner("Test2")
        c = Controller()
        c.player_repository.add(attacker)
        c.player_repository.add(enemy)
        res = c.fight("Test1", "Test2")
        self.assertEqual(res, "Attack user health 250 - Enemy user health 90")

    def test_report(self):
        attacker = Advanced("Test1")
        enemy = Beginner("Test2")
        c = Controller()
        c.player_repository.add(attacker)
        c.player_repository.add(enemy)
        res = c.report()
        self.assertEqual(res, "Username: Test1 - Health: 250 - Cards 0\nUsername: Test2 - Health: 50 - Cards 0\n")

