from project.card.card import Card


class MagicCard(Card):
    default_card_damage_points = 5
    default_card_health_points = 80

    def __init__(self, name):
        super().__init__(name, self.default_card_damage_points, self.default_card_health_points)
