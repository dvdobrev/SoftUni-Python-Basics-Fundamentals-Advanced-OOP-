from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        searched_player = [p for p in self.players if p.username == player.username]
        if searched_player:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        searched_player = [p for p in self.players if p.username == player][0]
        self.players.remove(searched_player)
        self.count -= 1

    def find(self, username: str):
        searched_player = [p for p in self.players if p.username == username][0]
        return searched_player
