from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    default_room_cost = 15
    default_appliances = [TV(), Fridge(), Stove()]


    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one + pension_two, 2)
        self.room_cost = self.default_room_cost
        self.expenses = self.calculate_expenses(self.get_appliances())

    def get_appliances(self):
        list_appliances = []
        for i in range(self.members_count):
            for a in self.default_appliances:
                list_appliances.append(a)
        return list_appliances


# a = OldCouple("Dobrev", 200, 200)
# print(a.expenses)
