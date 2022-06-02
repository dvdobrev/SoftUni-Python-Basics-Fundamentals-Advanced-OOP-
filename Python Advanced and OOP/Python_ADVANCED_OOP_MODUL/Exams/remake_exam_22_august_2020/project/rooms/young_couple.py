from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    default_room_cost = 20
    default_appliances = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salaray_one: float, salaray_two: float):
        super().__init__(family_name, salaray_one + salaray_two, 2)
        self.room_cost = self.default_room_cost
        self.expenses = self.calculate_expenses(self.get_appliances())

    def get_appliances(self):
        list_appliances = []
        for i in range(self.members_count):
            for a in self.default_appliances:
                list_appliances.append(a)
        return list_appliances