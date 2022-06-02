from abc import ABC, abstractmethod


class Astronaut(ABC):

    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []
        #self.breath_reduce_oxygen = 10

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "" or value.isspace():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self._name = value

    def breathe(self):
        self.oxygen -= self.breath_reduce_oxygen

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
