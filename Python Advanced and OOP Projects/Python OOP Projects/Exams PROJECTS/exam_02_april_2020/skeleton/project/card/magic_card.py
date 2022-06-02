from project.card.card import Card


class MagicCard(Card):
    def __init__(self, name):
        Card.__init__(self, name, 5, 80)

#
# class MagicCard(Card):
#     default_damage_points = 5
#     default_health_points = 80
#
#     def __init__(self, name):
#         super().__init__(name, self.default_damage_points, self.default_health_points)
