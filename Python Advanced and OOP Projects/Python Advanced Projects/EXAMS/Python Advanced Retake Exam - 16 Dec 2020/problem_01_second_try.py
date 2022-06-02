males = [int(el) for el in input().split()]
females = [int(el) for el in input().split()]
match_count = 0

while True:

    if males and females:
        current_male = males[-1]
        current_female = females[0]

        if current_male <= 0:
            males.pop()
            continue

        if current_female <= 0:
            females.pop(0)
            continue

        if current_male % 25 == 0:
            males.pop()
            males.pop()
            continue

        if current_female % 25 == 0:
            females.pop(0)
            females.pop(0)
            continue

        if current_female == current_male:
            males.pop()
            females.pop(0)
            match_count += 1

        else:
            females.pop(0)
            current_male -= 2
            males[-1] = current_male

    else:
        break

print(f"Matches: {match_count}")

if males:
    print(f"Males left: ", end="")
    print(*males[::-1], sep=", ")

else:
    print(f"Males left: none")

if females:
    print(f"Females left: ", end="")
    print(*females, sep=", ")

else:
    print(f"Females left: none")