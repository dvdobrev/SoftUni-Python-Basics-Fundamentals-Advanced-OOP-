deck = input().split()
shuffle = int(input())
left_deck = []
right_deck = []
half_deck = int(len(deck)/2)

for sh in range(shuffle):
    current_deck = []
    left_deck = deck[0:half_deck]
    right_deck = deck[half_deck::]
    for card in range(len(left_deck)):
        current_deck.append(left_deck[card])
        current_deck.append(right_deck[card])
    deck = current_deck
print(deck)