from project.card.card import Card
from project.card.magic_card import MagicCard


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []
        self.cards_total_damage = self.get_card_total_damage()

    def add(self, card: Card):
        searched_card = [c for c in self.cards if c.name == card.name]
        if searched_card:
            raise ValueError(f"Card {card.name} already exists!")

        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError(f"Card cannot be an empty string!")
        searched_card = [c for c in self.cards if c.name == card][0]
        self.cards.remove(searched_card)
        self.count -= 1

    def find(self, name: str):
        searched_card = [c for c in self.cards if c.name == name][0]
        return searched_card

    def get_card_total_damage(self):
        total_damage = sum([c.damage_points for c in self.cards])
        return total_damage

