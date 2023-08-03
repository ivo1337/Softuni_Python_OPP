from project.hero import Hero
import unittest

class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Test", 1, 100, 100)

    def test_init(self):
        self.assertEqual(self.hero.username, "Test")
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 100)

    def test_battle_yourself(self):
        enemy_hero = Hero("Test", 1, 100, 100)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_your_health_is_zero(self):
        enemy_hero = Hero("Enemy", 1, 100, 100)
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_enemy_hero_health_is_zero(self):
        enemy_hero = Hero("Enemy", 1, 100, 100)
        enemy_hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(ex.exception), "You cannot fight Enemy. He needs to rest")

    def test_draw(self):
        enemy_hero = Hero("Enemy", 1, 100, 100)
        self.assertEqual(self.hero.battle(enemy_hero), "Draw")

    def test_win(self):
        enemy_hero = Hero("Enemy", 1, 50, 50)
        self.assertEqual(self.hero.battle(enemy_hero), "You win")
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 55)
        self.assertEqual(self.hero.damage, 105)

    def test_lose(self):
        enemy_hero = Hero("Enemy", 1, 150, 150)
        self.assertEqual(self.hero.battle(enemy_hero), "You lose")
        self.assertEqual(enemy_hero.level, 2)
        self.assertEqual(enemy_hero.health, 55)
        self.assertEqual(enemy_hero.damage, 155)

    def test_str(self):
        self.assertEqual(str(self.hero), "Hero Test: 1 lvl\nHealth: 100\nDamage: 100\n")
