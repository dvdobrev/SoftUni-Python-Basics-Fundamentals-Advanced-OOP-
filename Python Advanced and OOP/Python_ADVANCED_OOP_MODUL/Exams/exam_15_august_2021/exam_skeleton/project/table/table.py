from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity  # table's seat capacity.
        self.food_orders = []  # every food order made from the table.
        self.drink_orders = []  # every drink order made from the table.
        self.number_of_people = 0  # the count of people who sit at the table. 0 by default.
        self.is_reserved = False  # Returns True if the table is reserved

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self._capacity = value

    def reserve(self, number_of_people: int):
        if not self.is_reserved:     # тука не бях сложил проверка дали е свободна масата
            self.is_reserved = True
            self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        bill = sum([f.price for f in self.food_orders]) + sum([d.price for d in self.drink_orders])
        bill = f"{bill:.2f}"
        bill = float(bill)
        return bill

        # he did it like this

        # bill = 0
        # bill += sum([f.price for f in self.food_orders])
        # bill += sum([d.price for d in self.drink_orders])
        # return bill

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False   # check if should be reserved

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\n" \
                   f"Type: {self.__class__.__name__}\n" \
                   f"Capacity: {self.capacity}"
