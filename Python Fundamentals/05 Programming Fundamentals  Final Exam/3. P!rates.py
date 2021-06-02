data = input()

cities_to_go = {}

while not data == "Sail":
    city, population, gold = data.split("||")
    population = int(population)
    gold = int(gold)

    if city not in cities_to_go:
        cities_to_go[city] = {}
        cities_to_go[city]["population"] = population
        cities_to_go[city]["gold"] = gold

    else:
        cities_to_go[city]["population"] += population
        cities_to_go[city]["gold"] += gold

    data = input()

events = input()

while not events == "End":
    events = events.split("=>")
    command = events[0]
    town = events[1]

    if command == "Plunder":
        killed_people = int(events[2])
        stolen_gold = int(events[3])
        cities_to_go[town]["population"] -= killed_people
        cities_to_go[town]["gold"] -= stolen_gold

        print(f"{town} plundered! {stolen_gold} gold stolen, {killed_people} citizens killed.")

        if cities_to_go[town]["population"] == 0 or  cities_to_go[town]["gold"] == 0:
            cities_to_go.pop(town)
            print(f"{town} has been wiped off the map!")

    else:
        gold = int(events[2])

        if gold > 0:
            cities_to_go[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities_to_go[town]['gold']} gold.")
        else:
            print(f"Gold added cannot be a negative number!")

    events = input()

sorted_cities = dict(sorted(cities_to_go.items(), key=lambda kvp: (-kvp[1]["gold"], kvp[0])))

print(f"Ahoy, Captain! There are {len(sorted_cities)} wealthy settlements to go to:")

for townn, population_gold in sorted_cities.items():
    print(f"{townn} -> Population: {population_gold['population']} citizens, Gold: {population_gold['gold']} kg")