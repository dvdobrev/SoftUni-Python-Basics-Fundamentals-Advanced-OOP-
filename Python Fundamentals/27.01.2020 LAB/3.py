card = input()

teamA_players_count = 11
teamB_players_count = 11
players_teamA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
players_teamB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
splited_card = card.split("-")

print(splited_card)

for i in splited_card:
    if teamB_players_count < 7 or teamA_players_count < 7:
        print(f"Team A - {teamA_players_count}; Team B - {teamB_players_count}")
        print("Game was terminated")
        break
    if i[0] == "A":
        if i[1] in players_teamA:
            teamA_players_count -= 1
            players_teamA.remove(i[1])
        else:
            continue

    elif i[0] == "B":
        if i[1] in players_teamB:
            teamB_players_count -= 1
            players_teamB.remove(i[1])
        else:
            continue
print(f"Team A - {teamA_players_count}; Team B - {teamB_players_count}")



