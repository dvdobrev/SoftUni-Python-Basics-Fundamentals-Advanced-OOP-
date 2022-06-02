from project.card.card import Card


class TrapCard(Card):
    default_card_damage_points = 120
    default_card_health_points = 5

    def __init__(self, name):
        super().__init__(name, self.default_card_damage_points, self.default_card_health_points)