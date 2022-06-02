from project.player.player import Player


class Beginner(Player):
    default_health_points = 50

    def __init__(self, username):
        super().__init__(username, self.default_health_points)
