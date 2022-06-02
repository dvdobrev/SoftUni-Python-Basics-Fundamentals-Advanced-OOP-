from project.card.card import Card


class TrapCard(Card):
    def __init__(self, name):
        Card.__init__(self, name, 120, 5)



#
# class TrapCard(Card):
#     default_damage_points = 120
#     default_health_points = 5
#
#     def __init__(self, name):
#         super().__init__(name, self.default_damage_points, self.default_health_points)