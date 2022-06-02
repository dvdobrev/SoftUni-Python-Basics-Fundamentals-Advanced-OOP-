from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    default_room_cost = 10
    default_appliances = [TV()]

    def __init__(self, name: str, salary):
        super().__init__(name, salary, 1)
        self.room_cost = self.default_room_cost
        self.expenses = self.calculate_expenses(self.default_appliances)
