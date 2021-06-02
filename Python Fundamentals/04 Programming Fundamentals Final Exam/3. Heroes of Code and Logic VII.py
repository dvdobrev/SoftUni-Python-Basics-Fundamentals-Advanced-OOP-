n = int(input())
heroes = {}

for _ in range(n):
    heroes_name, hit_points_to_recover, mana_points = input().split()
    heroes[heroes_name] = [hit_points_to_recover, mana_points]

command = input()

while not command == "End":
    command = command.split(" - ")
    if command[0] == "CastSpell":
        hero_name = command[1]
        mana_cast_points = int(command[2])
        spell_name = command[3]
        heroes_mana = int(heroes[hero_name][1])
        if heroes_mana >= mana_cast_points:
            heroes_mana -= mana_cast_points
            heroes[hero_name][1] = heroes_mana
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_mana} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command[0] == "TakeDamage":
        hero_name = command[1]
        damage_points = int(command[2])
        attacker = command[3]
        hero_hit_points = int(heroes[hero_name][0])
        hero_hit_points -= damage_points
        if hero_hit_points > 0:
            heroes[hero_name][0] = hero_hit_points
            print(f"{hero_name} was hit for {damage_points} HP by {attacker} and now has {hero_hit_points} HP left!")
        else:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif command[0] == "Recharge":
        hero_name = command[1]
        mana_points_to_recharge = int(command[2])
        heroes_mana = int(heroes[hero_name][1])
        heroes_mana += mana_points_to_recharge
        if heroes_mana > 200:
            rechared_points = 200 - (heroes_mana - mana_points_to_recharge)
            heroes_mana = 200
            print(f"{hero_name} recharged for {rechared_points} MP!")
        else:
            print(f"{hero_name} recharged for {mana_points_to_recharge} MP!")
        heroes[hero_name][1] = heroes_mana

    elif command[0] == "Heal":
        hero_name = command[1]
        hit_points_to_recover = int(command[2])
        hero_hit_points = int(heroes[hero_name][0])
        hero_hit_points += hit_points_to_recover
        if hero_hit_points > 100:
            healed_points = 100 - (hero_hit_points - hit_points_to_recover)
            hero_hit_points = 100
            print(f"{hero_name} healed for {healed_points} HP!")
        else:
            print(f"{hero_name} healed for {hit_points_to_recover} HP!")

        heroes[hero_name][0] = hero_hit_points

    command = input()

for k, v in heroes.items():
    int_num = []
    for num in v:
        num = int(num)
        int_num.append(num)
    heroes[k] = int_num

sorted_heroes = dict(sorted(heroes.items(), key=lambda kvp: (-kvp[1][0], kvp[0])))

for hero, hp_mp in sorted_heroes.items():
    print(hero)
    print(f"  HP: {hp_mp[0]}")
    print(f"  MP: {hp_mp[1]}")