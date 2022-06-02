class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value

    def calculate_expenses(self, *args):
        total_cost = 0
        for arg in args:
            for el in arg:
                total_cost += el.cost * 30
        return total_cost

    @property
    def total_expenses(self):
        return self.expenses + self.room_cost
