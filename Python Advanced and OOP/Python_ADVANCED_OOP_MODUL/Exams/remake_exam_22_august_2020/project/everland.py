from new_test_project.project.room import Child
from project.rooms.room import Room
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum(r.total_expenses for r in self.rooms)
        return f"Monthly consumption: {total_consumption}$."

    def pay(self):
        pass

    def status(self):
        pass
