from project.player.player import Player


class BattleField:

    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if attacker.__class__.__name__ == "Beginner":
            self.check_if_player_is_beginner(attacker)

        if enemy.__class__.__name__ == "Beginner":
            self.check_if_player_is_beginner(enemy)

        attacker.health += self.get_bonus_health_points(attacker)
        enemy.health += self.get_bonus_health_points(enemy)

        for card in attacker.card_repository.cards:
            if attacker.is_dead or enemy.is_dead:
                return
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            if attacker.is_dead or enemy.is_dead:
                return
            attacker.take_damage(card.damage_points)

    @staticmethod
    def check_if_player_is_beginner(player: Player):
        if player.__class__.__name__ == "Beginner":
            player.health += 40
            for card in player.card_repository.cards:
                card.damage_points += 30

    @staticmethod
    def get_bonus_health_points(player: Player):
        bonus_points = sum(c.health_points for c in player.card_repository.cards)
        return bonus_points

    @staticmethod
    def total_damage_points(player: Player):
        total_dm_points = sum(c.damage_points for c in player.card_repository.cards)
        return total_dm_points

#
# from project.player.player import Player
#
#
# class BattleField:
#     @staticmethod
#     def fight(attacker: Player, enemy: Player):
#         if attacker.is_dead or enemy.is_dead:
#             raise ValueError("Player is dead!")
#
#         if attacker.__class__.__name__ == "Beginner":
#             attacker.health += 40
#             for card in attacker.card_repository.cards:
#                 card.damage_points += 30
#
#         if enemy.__class__.__name__ == "Beginner":
#             enemy.health += 40
#             for card in enemy.card_repository.cards:
#                 card.damage_points += 30
#
#         attacker.health += sum([c.health_points for c in attacker.card_repository.cards])
#         enemy.health += sum([c.health_points for c in enemy.card_repository.cards])
#
#         for card in attacker.card_repository.cards:
#             if attacker.is_dead or enemy.is_dead:
#                 return
#             enemy.take_damage(card.damage_points)
#
#         for card in enemy.card_repository.cards:
#             if attacker.is_dead or enemy.is_dead:
#                 return
#             attacker.take_damage(card.damage_points)
