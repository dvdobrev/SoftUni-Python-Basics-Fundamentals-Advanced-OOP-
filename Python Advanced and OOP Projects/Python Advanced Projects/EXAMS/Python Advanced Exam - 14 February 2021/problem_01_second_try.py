firework_effects = [int(el) for el in input().split(", ")]  # first effect
explosive_power = [int(el) for el in input().split(", ")]  # with last power

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0
is_succesful = False

while True:
    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        is_succesful = True
        break
    if not firework_effects or not explosive_power:
        break

    current_effect = firework_effects[0]
    current_power = explosive_power[-1]
    total_sum = current_effect + current_power

    if current_effect <= 0:
        firework_effects.pop(0)
        continue

    if current_power <= 0:
        explosive_power.pop()
        continue

    if total_sum % 3 == 0 and not total_sum % 5 == 0:
        firework_effects.pop(0)
        explosive_power.pop()
        palm_fireworks += 1

    elif total_sum % 5 == 0 and not total_sum % 3 == 0:
        firework_effects.pop(0)
        explosive_power.pop()
        willow_fireworks += 1

    elif total_sum % 5 == 0 and total_sum % 3 == 0:
        firework_effects.pop(0)
        explosive_power.pop()
        crossette_fireworks += 1

    else:
        current_effect -= 1
        firework_effects.append(current_effect)
        firework_effects.pop(0)

if is_succesful:
    print(f"Congrats! You made the perfect firework show!")

else:
    print(f"Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join([str(el) for el in firework_effects])}")

if explosive_power:
    print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")
