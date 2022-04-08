from unittest import TestCase, main
from project.hero import Hero


# username
# level
# health
# damage

class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Harry", 100, 200, 300)
        self.enemy = Hero("Ron", 100, 200, 300)
        self.strong_hero = Hero("Strong Harry", 1000, 200000, 3000)

    def test_init(self):
        self.assertEqual("Harry", self.hero.username)
        self.assertEqual(100, self.hero.level)
        self.assertEqual(200, self.hero.health)
        self.assertEqual(300, self.hero.damage)

    def test_battle_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_no_health(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_with_enemy_with_no_health(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_draft(self):
        res = self.hero.battle(self.enemy)
        self.assertEqual(res, "Draw")


    def test_win_battle(self):
        res = self.strong_hero.battle(self.enemy)
        self.assertEqual(res, "You win")
        self.assertEqual(170005, self.strong_hero.health)
        self.assertEqual(3005, self.strong_hero.damage)
        self.assertEqual(1001, self.strong_hero.level)

        self.assertEqual(-2999800, self.enemy.health)
        self.assertEqual(300, self.enemy.damage)
        self.assertEqual(100, self.enemy.level)

    def test_lose_battle(self):
        res = self.enemy.battle(self.strong_hero)
        self.assertEqual(res, "You lose")
        self.assertEqual(170005, self.strong_hero.health)
        self.assertEqual(3005, self.strong_hero.damage)
        self.assertEqual(1001, self.strong_hero.level)

        self.assertEqual(-2999800, self.enemy.health)
        self.assertEqual(300, self.enemy.damage)
        self.assertEqual(100, self.enemy.level)

    def test_str(self):
        self.assertEqual("Hero Harry: 100 lvl\nHealth: 200\nDamage: 300\n", str(self.hero))

if __name__ == '__main__':
    main()

# level  5 , 10
# health  100, 80
# damage  10, 20
