team_a = 11
team_b = 11
players_wtih_cards_a = []
players_wtih_cards_b = []
cards = input().split()
game_terminated = False
for card in cards:
    if  "A" in card:
        if not card in players_wtih_cards_a:
            team_a -= 1
            players_wtih_cards_a.append(card)
    else:
        if "B" in card:
            if not card in players_wtih_cards_b:
                team_b -= 1
                players_wtih_cards_b.append(card)

    if team_a < 7 or team_b < 7:
        game_terminated = True
        break

print(f"Team A - {team_a}; Team B - {team_b}")
if game_terminated:
    print("Game was terminated")
