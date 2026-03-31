import unittest

from project.hero import Hero


class HeroTests(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Pesho", 10, 100.0, 20.0)
        self.enemy = Hero("Gosho", 10, 100.0, 20.0)

    def test_init(self):
        self.assertEqual("Pesho", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(20.0, self.hero.damage)

    def test_battle_raises_exception_when_fighting_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_raises_value_error_when_hero_health_is_zero_or_less(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_raises_value_error_when_enemy_health_is_zero_or_less(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_returns_draw_when_both_heroes_die(self):
        hero = Hero("Pesho", 1, 10, 10)
        enemy = Hero("Gosho", 1, 10, 10)

        result = hero.battle(enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(0, hero.health)
        self.assertEqual(0, enemy.health)

    def test_battle_hero_wins(self):
        hero = Hero("Pesho", 2, 100, 50)
        enemy = Hero("Gosho", 1, 50, 10)

        result = hero.battle(enemy)

        self.assertEqual("You win", result)
        self.assertEqual(3, hero.level)
        self.assertEqual(95, hero.health)
        self.assertEqual(55, hero.damage)
        self.assertEqual(-50, enemy.health)

    def test_battle_hero_loses(self):
        hero = Hero("Pesho", 1, 50, 10)
        enemy = Hero("Gosho", 2, 100, 50)

        result = hero.battle(enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(3, enemy.level)
        self.assertEqual(95, enemy.health)
        self.assertEqual(55, enemy.damage)
        self.assertEqual(-50, hero.health)

    def test_str_returns_correct_result(self):
        expected = "Hero Pesho: 10 lvl\nHealth: 100.0\nDamage: 20.0\n"
        self.assertEqual(expected, str(self.hero))


if __name__ == "__main__":
    unittest.main()