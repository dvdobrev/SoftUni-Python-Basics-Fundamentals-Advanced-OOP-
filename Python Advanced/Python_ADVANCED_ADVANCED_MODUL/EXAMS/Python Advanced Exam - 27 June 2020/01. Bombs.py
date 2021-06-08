from collections import deque

bomb_effekt = deque(int(el) for el in input().split(", "))
bomb_casing = deque(int(el) for el in input().split(", "))

cherry_bombs = 0
datura_bombs = 0
smoke_decoy_bombs = 0

while True:
    if cherry_bombs >= 3 and datura_bombs >= 3 and smoke_decoy_bombs >= 3:
        break

    if bomb_effekt and bomb_casing:
        current_bomb_effekt = bomb_effekt[0]
        current_casing_effekt = bomb_casing[-1]

        if current_bomb_effekt + current_casing_effekt == 40:
            datura_bombs += 1
            bomb_effekt.popleft()
            bomb_casing.pop()

        elif current_bomb_effekt + current_casing_effekt == 60:
            cherry_bombs += 1
            bomb_effekt.popleft()
            bomb_casing.pop()

        elif current_bomb_effekt + current_casing_effekt == 120:
            smoke_decoy_bombs += 1
            bomb_effekt.popleft()
            bomb_casing.pop()

        else:

            bomb_casing[-1] -= 5

    else:
        break
        

if cherry_bombs >= 3 and datura_bombs >= 3 and smoke_decoy_bombs >= 3:
    print(f"Bene! You have successfully filled the bomb pouch!")

else:
    print(f"You don't have enough materials to fill the bomb pouch.")


if bomb_effekt:
    print("Bomb Effects: ", end="")
    print(*bomb_effekt, sep=", ")

else:
    print("Bomb Effects: empty")


if bomb_casing:
    print("Bomb Casings: ", end="")
    print(*bomb_casing, sep=", ")

else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")