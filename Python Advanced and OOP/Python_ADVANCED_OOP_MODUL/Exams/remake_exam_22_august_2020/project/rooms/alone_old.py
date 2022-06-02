from project.rooms.room import Room


class AloneOld(Room):
    default_room_cost = 10

    def __init__(self, name: str, pension):
        super().__init__(name, pension, 1)
        self.room_cost = self.default_room_cost
