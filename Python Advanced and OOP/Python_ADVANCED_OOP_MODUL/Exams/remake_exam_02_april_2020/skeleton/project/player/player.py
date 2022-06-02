from abc import ABC, abstractmethod

from project.card.card_repository import CardRepository


class Player(ABC):
    @abstractmethod
    def __init__(self, username, health):
        self.username = username
        self.health = health
        self.card_repository = CardRepository()


    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Player's username cannot be an empty string.")
        self._username = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")
        self._health = value

    @property
    def is_dead(self):
        return True if self.health <= 0 else False

    def take_damage(self, damage_points: int):
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")
        self.health -= damage_points



___________________________


from project.survivor import Survivor


class Bunker:

    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []
        self.food = []
        self.water = []
        self.painkillers = []
        self.salves = []

    @property
    def food(self):
        return self._food

    @food.setter
    def food(self, value):
        foods = [f for f in self.supplies if f.__class__.__name__ == "FoodSupply"]
        if not foods:
            raise ValueError("There are no food supplies left!")
        self._food = foods

    @property
    def water(self):
        return self._water

    @water.setter
    def water(self, value):
        water = [w for w in self.supplies if w.__class__.__name__ == "WaterSupply"]
        if not water:
            raise ValueError("There are no water supplies left!")

        self._water = water

    @property
    def painkillers(self):
        return self._painkillers

    @painkillers.setter
    def painkillers(self, value):
        painkillers = [p for p in self.supplies if p.__class__.__name__ == "Painkiller"]
        if not painkillers:
            raise ValueError("There are no painkillers left!")
        self._painkillers = painkillers

    @property
    def salves(self):
        return self._salves

    @salves.setter
    def salves(self, value):
        salves = [s for s in self.supplies if s.__class__.__name__ == "Salve"]
        if not salves:
            raise ValueError("There are no salves left!")
        self._salves = salves


    def add_survivor(self, survivor: Survivor):
        pass

_________________________________

class Survivor:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.health = 100
        self.needs = 100

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age not valid!")

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0 or value > 100:
            self._health = 100
            raise ValueError("Health not valid!")
        self._health = value

    @property
    def needs(self):
        return self._health

    @needs.setter
    def needs(self, value):
        if value < 0 or value > 100:
            self._needs = 100
            raise ValueError("Needs not valid!")
        self._needs = value

    @property
    def needs_sustenance(self):
        return True if self.needs < 100 else False

    @property
    def needs_healing(self):
        return True if self.health < 100 else False



___________________________________


from abc import ABC, abstractmethod


class Medicine(ABC):
    @abstractmethod
    def __init__(self, health_increase):
        self.health_increase = health_increase

    @property
    def health_increase(self):
        return self._health_increase

    @health_increase.setter
    def health_increase(self, value):
        if value < 0:
            raise ValueError("Health increase cannot be less than zero.")
        self._health_increase = value


    def apply(self, survivor: Survivor):
        pass


____________________________

from abc import ABC, abstractmethod


class Supply(ABC):
    @abstractmethod
    def __init__(self, needs_increase: int):
        self.needs_increase = needs_increase

    @property
    def needs_increase(self):
        return self._needs_increase

    @needs_increase.setter
    def needs_increase(self, value):
        if value < 0:
            raise ValueError("Needs increase cannot be less than zero.")

        self._needs_increase = value

    def apply(self, survivor: Survivor):
        pass




