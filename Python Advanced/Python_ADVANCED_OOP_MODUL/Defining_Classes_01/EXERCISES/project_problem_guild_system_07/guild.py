from Python_ADVANCED_OOP_MODUL.Defining_Classes_01.EXERCISES.project_Guild_system_07.player import Player

"""
When you submit in Judge, you have to:
1. Create a whole new folder named 'project' out of any other folders.
2. The import path (the first line) should be exactly the same as 'from project.player import Player'!!!
3. Make a zip file.
"""


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if not player.guild == self.name and not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."

        filtered_players = [p for p in self.players if p == player]
        if filtered_players:
            return f"Player {player.name} is already in the guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        filtered_players = [p for p in self.players if p.name == player_name]
        if not filtered_players:
            return f"Player {player_name} is not in the guild."

        player = filtered_players[0]
        self.players.remove(player)
        player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        res = f"Guild: {self.name}\n"
        for p in self.players:
            res += p.player_info()
        return res

# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
#print(guild.kick_player("George"))
