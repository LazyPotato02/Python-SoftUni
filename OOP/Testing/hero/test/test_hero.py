from unittest import TestCase, main

from hero.project.hero import Hero


class HeroTest(TestCase):
    ATTACKER_USERNAME = 'ATTACKER'
    ATTACKER_LEVEL = 10
    ATTACKER_HEALTH = 100
    ATTACKER_DAMAGE = 75

    BATTLE_LEVEL_INCREMENT = 1
    BATTLE_HEALTH_INCREMENT = 5
    BATTLE_DAMAGE_INCREMENT = 5

    def setUp(self) -> None:
        self.attacker = Hero(self.ATTACKER_USERNAME, self.ATTACKER_LEVEL, self.ATTACKER_HEALTH, self.ATTACKER_DAMAGE)

    def test_hero_init(self):
        self.assertEqual(self.ATTACKER_USERNAME, self.attacker.username)
        self.assertEqual(self.ATTACKER_LEVEL, self.attacker.level)
        self.assertEqual(self.ATTACKER_HEALTH, self.attacker.health)
        self.assertEqual(self.ATTACKER_DAMAGE, self.attacker.damage)

    def test_battle_raises_when_attacker_enemy_with_same_username(self):
        enemy = Hero(self.ATTACKER_USERNAME, 5, 20, 30)

        with self.assertRaises(Exception) as error:
            self.attacker.battle(enemy)

        self.assertEqual("You cannot fight yourself", str(error.exception))

    def test_battle_raises_when_attacker_is_dead(self):
        enemy = Hero("Enemy", 5, 20, 30)
        self.attacker.health = 0

        with self.assertRaises(ValueError) as error:
            self.attacker.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

    def test_battle_raises_when_enemy_is_dead(self):
        enemy = Hero("Enemy", 5, 0, 30)

        with self.assertRaises(ValueError) as error:
            self.attacker.battle(enemy)

        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(error.exception))

    def test_battle_returns_draw_when_both_heroes_dies(self):
        enemy = Hero("Enemy", self.ATTACKER_LEVEL, self.ATTACKER_HEALTH, self.ATTACKER_DAMAGE)

        result = self.attacker.battle(enemy)
        expected_health = self.ATTACKER_HEALTH - (self.ATTACKER_LEVEL * self.ATTACKER_DAMAGE)
        self.assertEqual("Draw", result)
        self.assertEqual(expected_health, self.attacker.health)
        self.assertEqual(expected_health, enemy.health)

    def test_battle_returns_win_when_enemy_dies(self):
        enemy_level, enemy_health, enemy_damage = 5, 100, 10
        enemy = Hero("Enemy", enemy_level, enemy_health, enemy_damage)

        result = self.attacker.battle(enemy)
        enemy_expected_health = enemy_health - (self.ATTACKER_LEVEL * self.ATTACKER_DAMAGE)
        attacker_expected_level = self.ATTACKER_LEVEL + self.BATTLE_LEVEL_INCREMENT
        attacker_expected_damage = self.ATTACKER_DAMAGE + self.BATTLE_DAMAGE_INCREMENT
        attacker_expected_health = self.ATTACKER_HEALTH - (enemy_level * enemy_damage) + self.BATTLE_HEALTH_INCREMENT

        self.assertEqual("You win", result)
        self.assertEqual(enemy_expected_health, enemy.health)
        self.assertEqual(attacker_expected_level, self.attacker.level)
        self.assertEqual(attacker_expected_damage, self.attacker.damage)
        self.assertEqual(attacker_expected_health, self.attacker.health)

    def test_battle_returns_win_when_attacker_dies(self):
        attacker_level, attacker_health, attacker_damage = 5, 100, 10
        attacker = Hero("Attacker", attacker_level, attacker_health, attacker_damage)

        enemy = Hero("Enemy", self.ATTACKER_LEVEL, self.ATTACKER_HEALTH, self.ATTACKER_DAMAGE)

        result = attacker.battle(enemy)
        attacker_expected_health = attacker_health - (self.ATTACKER_LEVEL * self.ATTACKER_DAMAGE)
        enemy_expected_level = self.ATTACKER_LEVEL + self.BATTLE_LEVEL_INCREMENT
        enemy_expected_damage = self.ATTACKER_DAMAGE + self.BATTLE_DAMAGE_INCREMENT
        enemy_expected_health = self.ATTACKER_HEALTH - (attacker_level * attacker_damage) + self.BATTLE_HEALTH_INCREMENT

        self.assertEqual("You lose", result)
        self.assertEqual(attacker_expected_health, attacker.health)
        self.assertEqual(enemy_expected_level, enemy.level)
        self.assertEqual(enemy_expected_damage, enemy.damage)
        self.assertEqual(enemy_expected_health, enemy.health)

    def test_hero_str_returns_proper_message(self):
        actual_result = str(self.attacker)
        expected_result = f"Hero {self.ATTACKER_USERNAME}: {self.ATTACKER_LEVEL} lvl\n" \
               f"Health: {self.ATTACKER_HEALTH}\n" \
               f"Damage: {self.ATTACKER_DAMAGE}\n"

        self.assertEqual(expected_result,actual_result)

if __name__ == "__main__":
    main()
