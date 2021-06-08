from collections import deque

effects = deque(int(el) for el in input().split(", "))
power = [int(el) for el in input().split(", ")]

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0


while effects and power:
    current_effect = effects.popleft()
    current_power = power[-1]
    total_power = current_effect + current_power

    if current_power <= 0:
        power.pop()
        effects.appendleft(current_effect)
        continue

    if current_effect <= 0:
        continue

    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        effects.appendleft(current_effect)
        break

    if total_power % 3 == 0 and not total_power % 5 == 0:
        palm_fireworks += 1
        power.pop()

    elif total_power % 5 == 0 and not total_power % 3 == 0:
        willow_fireworks += 1
        power.pop()

    elif total_power % 3 == 0 and total_power % 5 == 0:
        crossette_fireworks += 1
        power.pop()

    else:
        current_effect -= 1
        effects.append(current_effect)


if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
    print(f"Congrats! You made the perfect firework show!")

else:
    print(f"Sorry. You can’t make the perfect firework show.")


if effects:
    print(f"Firework Effects left:", end=" ")
    print(*[el for el in effects], sep=", ")

if power:
    print(f"Explosive Power left:", end=" ")
    print(*[el for el in power], sep=", ")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")