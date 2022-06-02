from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    valid_astroanuts_types = ["Biologist", "Geodesist", "Meteorologist"]

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.completed_mission = 0
        self.not_completed_mission = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        searched_astronaut = [a for a in self.astronaut_repository.astronauts if a.name == name]

        if searched_astronaut:
            return f"{name} is already added."

        if astronaut_type not in self.valid_astroanuts_types:
            raise Exception("Astronaut type is not valid!")

        if astronaut_type == "Biologist":
            astronaut_to_add = Biologist(name)
            self.astronaut_repository.add(astronaut_to_add)

        elif astronaut_type == "Geodesist":
            astronaut_to_add = Geodesist(name)
            self.astronaut_repository.add(astronaut_to_add)

        else:
            astronaut_to_add = Meteorologist(name)
            self.astronaut_repository.add(astronaut_to_add)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items_to_add: str):
        searched_planet = [p for p in self.planet_repository.planets if p.name == name]
        items_as_list = [el for el in items_to_add.split(', ')]

        if searched_planet:
            return f"{name} is already added."

        planet = Planet(name)
        for el in items_as_list:
            planet.items.append(el)

        self.planet_repository.planets.append(planet)

    def retire_astronaut(self, name: str):
        searched_astronaut = [a for a in self.astronaut_repository.astronauts if a.name == name]
        if not searched_astronaut:
            raise Exception("Astronaut {astronaut_name} doesn't exists!")

        searched_astronaut = searched_astronaut[0]

        self.astronaut_repository.remove(searched_astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        searched_planet = [p for p in self.planet_repository.planets if p.name == planet_name]
        if not searched_planet:
            raise Exception("Invalid planet name!")

        searched_planet = searched_planet[0]

        suitable_astronauts = [a for a in self.astronaut_repository.astronauts if a.oxygen >= 30]
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        sorted_astronauts = sorted(suitable_astronauts, key=lambda a: a.oxygen, reverse=True)
        five_astronauts = sorted_astronauts[:5]

        items = searched_planet.items
        astronaut_count = 0
        for astronaut in five_astronauts:
            astronaut_count += 1

            while items:
                current_item = items.pop()
                astronaut.backpack.add(current_item)
                astronaut.breathe()

                if astronaut.oxygen <= 0:
                    break

        if not items:
            self.completed_mission += 1
            return f"Planet: {planet_name} was explored. {astronaut_count} astronauts participated in collecting items."

        else:
            self.not_completed_mission += 1
            return "Mission is not completed."

    def report(self):
        result = f"{self.completed_mission} successful missions!\n"
        result += f"{self.not_completed_mission} successful missions!\n"
        result += f"Astronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            result += f"Name: {astronaut.name}\n"
            result += f"Oxygen: {astronaut.oxygen}\n"
            result += f"Backpack items: "
            if astronaut.backpack:





# a = Meteorologist("dobri")
s = SpaceStation()
# print(s.add_astronaut("Biologist", "dobri"))
# print(s.add_astronaut("Biologist", "dobri"))
#
# print(s.add_astronaut("Geodesist", "geodesist test"))
# print(s.add_astronaut("Geodesist", "geodesist test"))
#
# print(s.add_astronaut("Meteorologist", "metro test"))
# print(s.add_astronaut("Meteorologist", "metro test"))
#

s.add_planet("merkurii", "kalii, 'magnezi")
a = 5
