class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.food_cost = food_cost
        self.toys_cost = toys_cost
        self.cost = self.calculate_total_cost()

    def calculate_total_cost(self):
        total_cost = self.food_cost + sum(self.toys_cost)
        return total_cost
