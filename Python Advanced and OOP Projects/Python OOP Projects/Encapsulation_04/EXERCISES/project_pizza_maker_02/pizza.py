from Python_ADVANCED_OOP_MODUL.Encapsulation_04.EXERCISES.project_pizza_maker_02.dough import Dough


class Pizza:
    def __init__(self, name, dough: Dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings = {}
        self.toppings_capacity = toppings_capacity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")

        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")

        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping):
        if len(self.toppings) < self.__toppings_capacity:
            if topping.topping_type not in self.toppings.keys():
                self.toppings[topping.topping_type] = 0
            self.toppings[topping.topping_type] += topping.weight

        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        result = self.dough.weight + sum(self.toppings.values())
        return result
