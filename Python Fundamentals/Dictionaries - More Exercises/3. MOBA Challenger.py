command = input()

players = {}
total_skill_points = {}

while not command == "Season end":
    if "vs" not in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in players:
            players[player] = {position: skill}
            total_skill_points[player] = skill
        else:
            if position not in players[player]:
                players[player][position] = skill
                total_skill_points[player] += skill
            else:
                if players[player][position] < skill:
                    total_skill_points[player] -= players[player][position]
                    total_skill_points[player] += skill
                    players[player][position] = skill

    else:
        player_1, player_2 = command.split(" vs ")
        if player_1 in players and player_2 in players:
            for key, value in players[player_1].items():
                if key in players[player_2].keys():
                    if total_skill_points[player_1] > total_skill_points[player_2]:
                        players.pop(player_2)
                        total_skill_points.pop(player_2)
                    elif total_skill_points[player_1] < total_skill_points[player_2]:
                        players.pop(player_1)
                        total_skill_points.pop(player_1)
                    break

    command = input()

sorted_players = dict(sorted(total_skill_points.items(), key=lambda kvp: (-kvp[1], kvp[0])))

for player, total_points in sorted_players.items():
    print(f"{player}: {total_points} skill")

    sorted_skills = dict(sorted(players[player].items(), key=lambda kvp: (-kvp[1], kvp[0])))
    for position, skill in sorted_skills.items():
        print(f"- {position} <::> {skill}")